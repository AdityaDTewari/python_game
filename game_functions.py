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

def update_bullets(bullets):
    """update the bullet position and get rid of old bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if under limit"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(ai_settings, screen, aliens):
    """create a fleet of aliens"""
    #we vreate an alien and find the number of aliens in a row
    #spacing between each alien will be equal to width of one alien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    #first row
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)