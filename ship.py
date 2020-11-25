import pygame

class Ship():

    def __init__(self, screen):
        """for ship initializing and setting the start position"""
        self.screen = screen

        #load the ship and set the rect
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect() #treating game elemnts as rectngles
        self.screen_rect = screen.get_rect()

        #starting a new ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx #working with the center attibute
        self.rect.bottom = self.screen_rect.bottom

        #movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """using the flag to update the position of the ship"""
        #moving the ship to the right by increasing the centrex attribute
        if self.moving_right:
            self.rect.centerx +=1
        if self.moving_left:
            self.rect.centerx -=1
    
    def blitme(self):
        """draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)