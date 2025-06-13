import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """class for game assets and behavior"""

    def __init__(self):
        """inits the game and game-resources"""

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Free My Boy E.T. 2025")
        self.ship = Ship(self)

        # background color
        self.bg_color = (0, 0, 0)
    
    def run_game(self):
        """main loop for the game"""

        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
        
    def _check_events(self):
        # watches for keyboard/mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def _update_screen(self):
        """updates images on the screen and flip to the new screen"""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # init game instance, and run game

    ai = AlienInvasion()
    ai.run_game()