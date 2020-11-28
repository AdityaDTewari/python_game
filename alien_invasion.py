import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initializing the game and creating a screen
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #Surface creation
    pygame.display.set_caption("Alien Invasion")

    #creating the ship
    ship = Ship(screen, ai_settings)

    #a group to store bullets
    bullets = Group()

    #set background color
    bg_color = (230, 230, 230) #light grey

    #start the main loop
    while True:
        #calling the class to check for events
        gf.check_events(ship, ai_settings, screen, bullets)
        
        #updating the ship centerx
        ship.update()

        #calling the update for each sprite in the group
        bullets.update()

        #getting rid of bullets that reach the top of the screen and update position
        gf.update_bullets(bullets)
        #print(len(bullets))

        #redraw the screen for each iteration and making the drawn circle visible
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()