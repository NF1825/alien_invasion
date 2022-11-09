import pygame
import sys
import time
from pygame.sprite import Sprite

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
        available_space_y = 600 - (2 * star_height)
        number_stars_x = available_space_x // (2 * star_width)
        number_rows = available_space_y // (2 * star_height)
        for rows in range(0,number_rows):
            for star_number in range(number_stars_x):
                star = Star(self)
                star.x = star_width + 2*star_width*star_number
                star.rect.x = star.x
                star.rect.y = star_height + 2 * star.rect.height * rows
                self.stars.add(star)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill((255,255,255))
        self.stars.draw(self.screen)

        pygame.display.flip()

    def update_stars(self):
        for star in self.stars.sprites():
            star.rect.y += 1

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.update_stars()



ev = Environment()
ev.run_game()







