import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """init the ship and set its starting pos"""
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship and get its "rect" rectangle
        self.image = pygame.image.load('images/shuttle2.png')
        self.rect = self.image.get_rect()

        # starts each ship at the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flags set to false; game starts with a motionless ship
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """updates the ships position based on the movement Flag"""

        # we use 2 if blocks instead of elif, so that when you press both left and right-
        # at the same time, the ship stays still. elif would give right key priority.
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
    
    def blitme(self):
        """draw the ship at its current location"""

        self.screen.blit(self.image, self.rect)