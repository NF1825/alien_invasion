import pygame
import sys
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self,ev_game):
        super().__init__()
        self.screen = ev_game.screen


        self.image = pygame.image.load("Gold_Star4.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.x = float(self.rect.x)



class Environment:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        self.stars = pygame.sprite.Group()

        self._create_starfield()

    def _create_starfield(self):
        star = Star(self)
        self.stars.add(star)
        star_width = star.rect.width
        available_space_x = 1200 - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)
        for star_number in range(number_stars_x):
            star = Star(self)
            star.x = star_width + 2*star_width*star_number
            star.rect.x = star.x
            self.stars.add(star)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill((255,255,255))
        self.stars.draw(self.screen)

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


ev = Environment()
ev.run_game()




