import sys
import pygame

class AlienInvasion:
    """Overall class for game assets and behavior"""

    def __init__(self):
        """initialize the game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1920,1080))
        pygame.display.set_caption("Alien Invasion")
        #set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            #make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()