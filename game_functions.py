import sys
import pygame

from bullet import Bullet

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

def update_screen(ai_settings, screen, ship, bullets, alien):
    """for redrawing the screen"""
    screen.fill(ai_settings.bg_color)

    #redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()

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