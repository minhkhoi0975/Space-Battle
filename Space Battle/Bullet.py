import pygame;
import random;
from pygame.sprite import Sprite;

class Bullet(Sprite):
    def __init__(self, settings, screen, astronaut):
        super().__init__();
        self.screen = screen;
        self.settings = settings;

        # If the astronaut looks to the right, the bullet must move to the right.
        if astronaut.isLookingToTheLeft == False:
            self.rect = pygame.Rect(astronaut.rect.right, astronaut.rect.top + 10, settings.bulletWidth, settings.bulletHeight);
            self.velocityX = settings.bulletSpeed;
        # If the astronaut looks to the left, the bullet must move to the left.
        else:
            self.rect = pygame.Rect(astronaut.rect.left - self.settings.bulletWidth, astronaut.rect.top + 10, settings.bulletWidth, settings.bulletHeight);
            self.velocityX = -settings.bulletSpeed;

        # Calculate the damage.
        self.damage = random.randint(settings.bulletBaseDamage - settings.bulletDamageDeviation, settings.bulletBaseDamage + settings.bulletDamageDeviation);

        # Bullet cannot harm its owner (the astronaut who shot it).
        self.owner = astronaut; 

    def update(self):
        self.rect.x += self.velocityX;

    def drawBullet(self):
        pygame.draw.rect(self.screen, self.settings.bulletColor, self.rect);
