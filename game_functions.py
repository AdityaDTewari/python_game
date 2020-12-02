import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    """updating the left/right flags, responding to keypress and firing the bullets"""
    if event.key == pygame.K_RIGHT:
        #ship.rect.centerx += 1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a bullet and add it to the group
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """updating the key releases"""
    if event.key == pygame.K_RIGHT:
            ship.moving_right = False
    elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(ship, ai_settings, screen, bullets):
    """for keyboard and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN: #keydown as the event to detect a keypress
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        
        elif event.type == pygame.KEYUP: #to know when the key is released
           check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets, aliens):
    """for redrawing the screen"""
    screen.fill(ai_settings.bg_color)

    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen) #each element is drawn in a group

    #making the drawn circle vivible
    pygame.display.flip()

def update_bullets(aliens, bullets):
    """update the bullet position and get rid of old bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    #check for any bullets that have hit aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) # both True for removing bullet and alien respectively after collision

def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if under limit"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """determine the number of rows that can fit in the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and place it in the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """create a fleet of aliens"""
    #we create an alien and find the number of aliens in a row
    #spacing between each alien will be equal to width of one alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    #first row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_aliens(ai_settings, aliens):
    """to update the position of all the aliens in the fleet
    after checking if the fleet is at the edge"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    """respond when fleet reaches the edges"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """drop the fleet and change its direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1