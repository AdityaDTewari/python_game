import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """representing a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #loading the image and setting the rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #alien at the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the exact position
        self.x = float(self.rect.x)
    
    def blitme(self):
        """draw the alien at current location"""
        self.screen.blit(self.image, self.rect)