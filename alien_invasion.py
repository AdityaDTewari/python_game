import sys
import pygame

from settings import Settings

def run_game():
    #initializing the game and creating a screen
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #Surface creation
    pygame.display.set_caption("Alien Invasion")

    #set background color
    bg_color = (230, 230, 230) #light grey

    #start the main loop
    while True:
        #for keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #redraw the screen for each iteration
        screen.fill(ai_settings.bg_color)

        #msking the drawn circle vivible
        pygame.display.flip()

run_game()