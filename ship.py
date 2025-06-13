import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """init the ship and set its starting pos"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship and get its "rect" rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # starts each ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """draw the ship at its current location"""

        self.screen.blit(self.image, self.rect)