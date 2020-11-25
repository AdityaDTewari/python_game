import sys
import pygame

def check_keydown_events(event, ship):
    """updating the left/right flags, responding to keypress"""
    if event.key == pygame.K_RIGHT:
        #ship.rect.centerx += 1
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    """updating the key releases"""
    if event.key == pygame.K_RIGHT:
            ship.moving_right = False
    elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(ship):
    """for keyboard and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN: #keydown as the event to detect a keypress
            check_keydown_events(event, ship)
        
        elif event.type == pygame.KEYUP: #to know when the key is released
           check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
    """for redrawing the screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #making the drawn circle vivible
    pygame.display.flip()