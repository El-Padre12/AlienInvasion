import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Alien class to manage alien fleet"""

    def __init__(self, ai_game):
        """inits the alien and sets starting position"""

        super().__init__()
        self.screen = ai_game.screen

        # loads image and sets it rect attribute
        self.image = pygame.image.load('images/ufo1.png')
        self.rect = self.image.get_rect()

        # starts each new alien on the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # stores the aliens exact horizontal position
        self.x = float(self.rect.x)