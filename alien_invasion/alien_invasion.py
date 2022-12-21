#!/usr/bin/env pyhon3

import sys
import pygame

class alienInvasion:
    
    def __init__(self):
        # Initialize game
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invation")
        
        # Set background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # Make screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvation()
    ai.rungame()
