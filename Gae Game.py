import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        pygame.display.set_caption('My gae game')
        self.ship = Ship(self)

    def game_start(self):
        
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    sys.exit()
        
            self.screen.fill(self.settings.background)
            self.ship.blitme()
            pygame.display.flip()
    
if __name__ == '__main__':
    game = AlienInvasion()
    game.game_start()