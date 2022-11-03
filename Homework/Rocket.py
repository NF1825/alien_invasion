import pygame
import sys

class Picture():
    def __init__(self,screen,image_address):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image_address)
        self.rect = self.image.get_rect()
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.exit = False
    def draw(self):
        self.rect.center = self.screen_rect.center
        self.screen.blit(self.image, self.rect)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.exit = True
                if event.key == pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.moving_left = True
                elif event.key == pygame.K_UP:
                    self.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.moving_left = False
                elif event.key == pygame.K_UP:
                    self.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.exit:
            sys.exit()
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1


pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))

rocket = Picture(screen, "rocket.bmp")

rocket.draw()

while True:
    rocket._check_events()
    screen.fill((255, 255, 255))
    if rocket.rect.right > rocket.screen_rect.right:
        rocket.moving_right = False
    if rocket.rect.left < 0:
        rocket.moving_left = False
    if rocket.rect.top < 0:
        rocket.moving_up = False
    if rocket.rect.bottom > rocket.screen_rect.bottom:
        rocket.moving_down = False
    rocket.update()
    rocket.blitme()
    pygame.display.flip()


