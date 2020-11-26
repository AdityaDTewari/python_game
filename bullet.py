import pygame
from pygame.sprite import Sprite #group related elements

class Bullet(Sprite):
    """to manage the bullets fireed from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet at the position of the ship"""
        super(Bullet, self).__init__()
        self.screen = screen

        #create a bullet at (0, 0) and then set position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) #building a rectangle
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #bullet position as a decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        """movement of the bullet"""
        self.y -= self.speed_factor
        #updating the rect
        self.rect.y = self.y
    
    def draw_bullet(self):
        """to draw the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)