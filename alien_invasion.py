import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
#from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #initializing the game and creating a screen
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #Surface creation
    pygame.display.set_caption("Alien Invasion")

    #make a play button
    play_button = Button(ai_settings, screen, "Play")

    #instance to store game statistics
    stats = GameStats(ai_settings)

    #creating an instance to store game statistics and create a scoreboard
    sb = Scoreboard(ai_settings, screen, stats)

    #creating the ship
    ship = Ship(screen, ai_settings)

    #creating the alien group
    #alien = Alien(ai_settings, screen)
    aliens = Group()

    #creating the alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #a group to store bullets
    bullets = Group()

    #set background color
    bg_color = (230, 230, 230) #light grey

    #start the main loop
    while True:
        #calling the class to check for events
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        
        if stats.game_active:
            #updating the ship centerx
            ship.update()

            #calling the update for each sprite in the group
            bullets.update()

            #getting rid of bullets that reach the top of the screen and update position
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #print(len(bullets))

            #updating the position of aliens in the fleet
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        #redraw the screen for each iteration and making the drawn circle visible
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)

run_game()