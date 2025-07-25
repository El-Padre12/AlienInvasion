import pygame.font

class Button:
    """Class for button objects - can be used for other games"""

    def __init__(self, ai_game, msg):
        """Inits button attributes"""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
    
        # button dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # build the buttons rect object and center it
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button message need be prepped only once
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Converts msg into rendered image and center text on button"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draws button to screen and draws text/msg to button"""

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)