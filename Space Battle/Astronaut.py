import pygame;
from pygame.sprite import Sprite;
from Bullet import Bullet;

class Astronaut():
    def __init__(self, settings, screen, walls, bullets, standingSprite, deathSprite):
        self.screen = screen;
        self.settings = settings;
        self.walls = walls;        # Reference to the list of all walls. 
        self.bullets = bullets;    # Reference to the list of all bullets. 

        # Load the sprites and scale them down by 50%.
        self.standingSprite = pygame.image.load(standingSprite);
        self.standingSprite = pygame.transform.rotozoom(self.standingSprite, 0.5, 0.5);
        self.deathSprite = pygame.image.load(deathSprite);
        self.deathSprite = pygame.transform.rotozoom(self.deathSprite, 0.5, 0.5);
        self.isLookingToTheLeft = False;

        # Set the current sprite to the standing sprite.
        self.currentSprite = self.standingSprite;
        self.rect = self.currentSprite.get_rect();
        self.screenRect = screen.get_rect();

        self.movingRight = False;
        self.movingLeft = False;
        self.movingUp = False;
        self.movingDown = False;

        self.health = settings.astronautHealth;
        self.totalKills = 0;
        self.consecutiveKills = 0;               # The number of consecutive kills the astronaut has without dying.
        self.greatestConsecutiveKills = 0;

    def update(self):
        # Move the astronaut horizontally.
        velocityX = 0;
        if self.movingRight:
            velocityX += self.settings.astronautSpeedX;
        if self.movingLeft:
            velocityX -= self.settings.astronautSpeedX;
        self.rect.x += velocityX;

        # If the x velocity and the direction the astronaut is looking at are not consistent, flip the image.
        if velocityX > 0 and self.isLookingToTheLeft:
            self.flipSprites();
            self.isLookingToTheLeft = False;
        if velocityX < 0 and self.isLookingToTheLeft == False:
            self.flipSprites();
            self.isLookingToTheLeft = True;

        # Check if the astronaut bumps into a wall. If he does, move him out of the wall.
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                if velocityX < 0:
                    self.rect.left = wall.rect.right;
                if velocityX > 0:
                    self.rect.right = wall.rect.left;
        
        # Move the astronaut vertically.
        velocityY = self.settings.astronautGravity;
        if self.movingUp:
            velocityY -= self.settings.astronautSpeedY;
        if self.movingDown:
            velocityY += self.settings.astronautSpeedY;
        self.rect.y += velocityY;

        # Check if the astronaut bumps into a wall. If he does, move him out of the wall.
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                if velocityY < 0:
                    self.rect.top = wall.rect.bottom;
                if velocityY > 0:
                    self.rect.bottom = wall.rect.top;
   
        # Do not let the astronaut get out of the screen.
        if self.rect.left < 0:
            self.rect.left = 0;
        if self.rect.right > self.settings.screenWidth:
            self.rect.right = self.settings.screenWidth;
        if self.rect.top < 0:
            self.rect.top = 0;
        if self.rect.bottom > self.settings.screenHeight:
            self.rect.bottom = self.settings.screenHeight;

    # Flip the sprites.
    def flipSprites(self):
        self.standingSprite = pygame.transform.flip(self.standingSprite, True, False);
        self.deathSprite = pygame.transform.flip(self.deathSprite, True, False);
        self.currentSprite = pygame.transform.flip(self.currentSprite, True, False);
    
    # Blit the sprite of the astronaut and his health bar to the screen.
    def blitMe(self):
        self.screen.blit(self.currentSprite, self.rect);

        if self.health > 0:
            healthBar = pygame.Rect(self.rect.left, self.rect.top - 10, self.rect.width * self.health / self.settings.astronautHealth, 5);
            pygame.draw.rect(self.screen, (255, 0, 0), healthBar);

    # The new bullet is included in the list of bullets.
    def fireBullet(self):
        bullet = Bullet(self.settings, self.screen, self);
        self.bullets.add(bullet);

    def die(self):
        # I die. I cannot move.
        self.movingLeft = False;
        self.movingRight = False;
        self.movingUp = False;
        self.movingDown = False;

        # Switch to dead image.
        positionX = self.rect.x;
        positionY = self.rect.y;
        self.currentSprite = self.deathSprite;
        self.rect = self.currentSprite.get_rect();
        self.rect.x = positionX;
        self.rect.y = positionY;

