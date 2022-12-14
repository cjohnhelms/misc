#!/usr/bin/env python3

import sys
import pygame

from settings import Settings
from ship import Ship

class alienInvasion:
    
    def __init__(self):
        # Initialize game
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance and run the game
    ai = alienInvasion()
    ai.run_game()
