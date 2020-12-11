import pygame;
from pygame.sprite import Sprite;

class Wall(Sprite):
    def __init__(self, screen, x, y, width, height, color):
        super().__init__();
        self.screen = screen;

        self.rect = pygame.Rect(x, y, width, height);
        self.color = color;

        #pygame.draw.rect(self.screen, self.color, self.rect);
    
    def drawWall(self):
        pygame.draw.rect(self.screen, self.color, self.rect);
        
