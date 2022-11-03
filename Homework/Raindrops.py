import pygame
import sys
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):

    def __init__(self,ev_game):
        super().__init__()
        self.screen = ev_game.screen


        self.image = pygame.image.load("raindrop.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += .5
        self.rect.y = self.y



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
        star_height = star.rect.height
        available_space_x = 1200 - (2 * star_width)
        available_space_y = 800 - (3*star_height)
        number_stars_y = available_space_y // (2*star_height)
        number_stars_x = available_space_x // (2 * star_width)
        for number_rows in range(number_stars_y):
            for star_number in range(number_stars_x):
                self._create_star(star_number,number_rows)

    def _create_star(self, star_number, number_rows):
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + 2 * star.rect.height * number_rows
        self.stars.add(star)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill((255,255,255))
        self.stars.draw(self.screen)
        self.stars.update()

        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


ev = Environment()
ev.run_game()
