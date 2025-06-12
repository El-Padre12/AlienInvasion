import sys
import pygame

class AlienInvasion:
    """class for game assets and behavior"""

    def __init__(self):
        """inits the game and game-resources"""

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Free My Boy E.T. 2025")
    
    def run_game(self):
        """main loop for the game"""

        while True:
            # watches for keyboard/mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # init game instance, and run game

    ai = AlienInvasion()
    ai.run_game()