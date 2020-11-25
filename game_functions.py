import sys
import pygame

def check_events(ship):
    """for keyboard and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN: #keydown as the event to detect a keypress
            #updating the left/right flags
            if event.key == pygame.K_RIGHT:
                #ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        
        elif event.type == pygame.KEYUP: #to know when the key is released
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """for redrawing the screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #making the drawn circle vivible
    pygame.display.flip()