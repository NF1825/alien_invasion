import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1200,600))
screen.fill((235,255,0))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
