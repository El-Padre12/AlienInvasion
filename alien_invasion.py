import sys # used to make the game exit when the player quits
import pygame # functionality needed to make a game

from settings import Settings
from ship import Ship

class AlienInvasion:
    """class for game assets and behavior"""

    def __init__(self):
        """inits the game and game-resources"""
        pygame.init()

        # assigning objects to attributes
        # the object assigned to 'self.screen' is a 'surface' in PyGame which represents an entire game window
        # a surface in Pygame is a part of the screen where a game element can be displayed
        # elements in the game such as 'alien' or 'ship' are surfaces
        self.clock = pygame.time.Clock()
        self.settings = Settings()        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Free My Boy E.T. 2025")
        self.ship = Ship(self)
    
    def run_game(self):
        """main loop for the game"""

        #event loop and code that manages screen updates
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60) # frame rate
            self.screen.fill(self.settings.bg_color)

    # helper methods do work inside a class but aren't meant to be used by code outside the class
    # in Python a single leading underscore indicates a helper method
    def _check_events(self):
        # watches for keyboard/mouse input from the user AKA 'events'
            for event in pygame.event.get():

                # clicking the close window button will exit game
                if event.type == pygame.QUIT:
                    sys.exit()
                # 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
    
    def _update_screen(self):
        """updates images on the screen and flip to the new screen"""
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
            
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # init game instance, and run game only if the file is called directly

    ai = AlienInvasion()
    ai.run_game()