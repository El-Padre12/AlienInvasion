import sys # used to make the game exit when the player quits
import pygame # functionality needed to make a game

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.screen = pygame.display.set_mode((1400,900)) # prefer this size over fullscreen
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Free My Boy E.T. 2025")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    
    def run_game(self):
        """main loop for the game"""

        #event loop and code that manages screen updates
        while True:
            self._check_events()
            
            self.ship.update()
            self.bullets.update()
            
            self._update_bullets()
            self._update_screen()
            
            self.clock.tick(60) # frame rate
            # self.screen.fill(self.settings.bg_color)

    # helper methods do work inside a class but aren't meant to be used by code outside the class
    # in Python a single leading underscore indicates a helper method
    def _check_events(self):
        # watches for keyboard/mouse input from the user AKA 'events'
            for event in pygame.event.get():

                # clicking the close window button will exit game
                if event.type == pygame.QUIT:
                    sys.exit()
                # handles ship movement
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """responds to key presses"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """responds to key releases"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """creates and adds new bullet to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
            """gets rid of bullets from memory when they "disapear" off the screen."""

            # updates bullet position
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _create_fleet(self):
        """creates alien fleet"""

        # make 1 alien and add aliens unil there is no more space
        # spacing = width of 1 alien
        alien = Alien(self)
        alien_width = alien.rect.width
        
        current_x = alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_alien(current_x)
            current_x += 2 * alien_width

    def _create_alien(self, x_pos):
        """create an alien and put it in a row"""

        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.rect.x = x_pos
        self.aliens.add(new_alien)

    def _update_screen(self):
        """updates images on the screen and flip to the new screen"""
        
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image, (0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
            
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # init game instance, and run game only if the file is called directly

    ai = AlienInvasion()
    ai.run_game()