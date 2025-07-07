import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet class to manages bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships current position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # create a bullet rect at (0,0) then set correct position
        # since the bullet is not a stored image we make the rect from-
        # scratch using "pygame.Rect()"
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # make bullets position a float
        self.y  = float(self.rect.y)
    
    def update(self):
        """moves the bullet up the screen"""

        # update the exact positon of the bullet
        self.y -= self.settings.bullet_speed

        # update the rect
        self.rect.y = self.y

    def draw_bullet(self):
        """draws the bullet to the screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)