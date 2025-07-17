class GameStats:
    """class that manages game stats for Alien Invasion"""

    def __init__(self, ai_game):
        """Inits stats"""

        self.settings = ai_game.settings
        self.reset_stats()
    
    def reset_stats(self):
        """Inits stats that can change during the game"""
        
        self.ships_left = self.settings.ship_limit