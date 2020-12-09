class GameStats():
    """tracking the statistics ofr the gmae"""

    def __init__(self, ai_settings):
        """initialize"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #start game in inactive state for the start button
        self.game_active = False
    
    def reset_stats(self):
        """initialize the statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0