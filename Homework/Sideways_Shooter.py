# code
import pygame
import sys
from pygame.sprite import Sprite

class Picture():
    def __init__(self):
        self.screen = pygame.display.set_mode((1100,600))
        self.bullets = pygame.sprite.Group()
        self.screen_rect = pygame.display.set_mode((1100,600)).get_rect()
        self.image = pygame.image.load("rocket2.bmp")
        self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.exit = False
    def draw(self):
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        self.screen.blit(self.image, self.rect)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.exit = True
                if event.key == pygame.K_UP:
                    self.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.exit:
            sys.exit()
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1

class Bullet(Sprite):

    def __init__(self, pic_game):

        super().__init__()
        self.screen = pic_game.screen
        self.color = (0,0,0)

        self.rect = pygame.Rect(0,0, 10, 3)
        self.rect.midleft = pic_game.rect.midright

        self.x = float(self.rect.x)
    def update(self):
        self.x += .5
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


pygame.init()
pic = Picture()
screen = pygame.display.set_mode((1100,600))
screen.fill((255,255,255))

rocket = Picture()

rocket.draw()

while True:
    rocket._check_events()
    screen.fill((255, 255, 255))
    if rocket.rect.top < 0:
        rocket.moving_up = False
    if rocket.rect.bottom > rocket.screen_rect.bottom:
        rocket.moving_down = False
    rocket.update()
    rocket.bullets.update()

    for bullet in rocket.bullets.copy():
        if bullet.rect.left > rocket.screen_rect.right:
            rocket.bullets.remove(bullet)

    rocket.blitme()
    for bullet in rocket.bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


