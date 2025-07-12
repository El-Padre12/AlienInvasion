import pygame

class Settings:
    """Alien Invasion settings class"""

    def __init__(self):
        """init game settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230 ,230)

        # Load background image
        self.bg_image = pygame.image.load('images/space1.jpg')
        self.bg_image = pygame.transform.scale(self.bg_image, (1400, 900))  # Scale to screen size

        # ship settings
        self.ship_speed = 4.8

        # bullet settings
        self.bullet_speed = 5.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 230, 230)
        self.bullets_allowed = 3