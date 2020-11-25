import pygame

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
    ship = Ship(screen)

    #set background color
    bg_color = (230, 230, 230) #light grey

    #start the main loop
    while True:
        #calling the class to check for events
        gf.check_events(ship)
        
        #updating the ship centerx
        ship.update()
        
        #redraw the screen for each iteration and making the drawn circle visible
        gf.update_screen(ai_settings, screen, ship)

run_game()