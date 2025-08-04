import sys # used to make the game exit when the player quits
from time import sleep # used to pause game for a moment when ship is hit

import pygame # functionality needed to make a game

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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
        pygame.display.set_caption("Free My Boy E.T. - © 2025 an Angel N Chavez Production")

        # create an instance to store game statistics, and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # game active flag set to true
        self.game_active = False

        # make the play button
        self.play_button = Button(self, 'Play')
    
    def run_game(self):
        """main loop for the game"""

        #event loop and code that manages screen updates
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
            
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """starts new game when the player clicks Play"""

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            self._start_game()     

    def _start_game(self):
        # reset the game settings
        self.settings.initialize_dynamic_settings()

        # reset game stats
        self.stats.reset_stats()

        # set game state to active/True
        self.game_active = True

        # get rid of remaining bullets and aliens
        self.bullets.empty()
        self.aliens.empty()

        # reset fleet and center ship
        self._create_fleet()
        self.ship.center_ship()

        # makes cursor invisible while game is active
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """responds to key presses"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            if not self.game_active:
                self._start_game()
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
            
            self._check_bullet_alien_collision()
    
    def _check_bullet_alien_collision(self):
            """respond to bullet-alien collision."""

            # check for any bullets that hit an alien, and get rid of alien and bullet if true
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

            if not self.aliens:
                self.bullets.empty()
                self._create_fleet()
                self.settings.increase_speed()

    def _update_aliens(self):
        """checks to see if fleet is at the edge, then updates postion"""

        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # look for aliens reaching the bottom of the screen
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom of the screen."""

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _create_fleet(self):
        """creates alien fleet"""

        # make 1 alien and add aliens unil there is no more space
        # spacing = width & height of 1 alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x = alien_width
        current_y = alien_height

        while current_y < (self.settings.screen_height -3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # rest x-value and increment y-value once row is completed
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_pos, y_pos):
        """create an alien and put it in a row"""

        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """response/action to any alien reaching the edge"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """drops entire fleet and changes fleet direction"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """responds to a ship colliding with an alien"""

        if self.stats.ships_left > 0:
            # decrements ships left
            self.stats.ships_left -= 1

            # empties any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # create new fleet and center the new ship
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """updates images on the screen and flip to the new screen"""
        
        # self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image, (0,0))

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)

        # draw the score info
        self.sb.show_score()

        # draw the play button if game is inacive
        if not self.game_active:
            self.play_button.draw_button()
            
        # make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # init game instance, and run game only if the file is called directly

    ai = AlienInvasion()
    ai.run_game()