import pygame

class Ship():

    def __init__(self, screen):
        """for ship initializing and setting the start position"""
        self.screen = screen

        #load the ship and set the rect
        self.image = pygame.image.load('images/space_ship.bmp')
        self.rect = self.image.get_rect() #treating game elemnts as rectngles
        self.screen_rect = screen.get_rect()

        #starting a new ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx #working with the center attibute
        self.rect.bottom = self.screen_rect.bottom

def blitme(self):
    """draw the ship at the current location"""
    self.screen.blit(self.image, self.rect)