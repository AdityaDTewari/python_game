class Settings():
    """a class to store the settings at one place"""

    def __init__(self):
        """initialize the setting of the game"""
        #screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship setings
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60