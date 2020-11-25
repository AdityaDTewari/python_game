import pygame

class Ship():

    def __init__(self, screen, ai_settings):
        """for ship initializing and setting the start position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship and set the rect
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect() #treating game elemnts as rectngles
        self.screen_rect = screen.get_rect()

        #starting a new ship at the bottom center
        self.rect.centerx = self.screen_rect.centerx #working with the center attibute
        self.rect.bottom = self.screen_rect.bottom

        #for storing the decimal value
        self.center = float(self.rect.centerx)

        #movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """using the flag to update the position of the ship"""
        #updaing the center value and not the rect and limiting the range of the ship
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #updating the rect from center
        self.rect.centerx = self.center
    
    def blitme(self):
        """draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)