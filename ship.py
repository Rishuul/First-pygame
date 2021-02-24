import pygame
class Ship:
    
    def __init__ (self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.ship = pygame.image.load('Assets/Ship.bmp')
        self.rect = self.ship.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.ship,self.rect)