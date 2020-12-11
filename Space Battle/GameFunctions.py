import sys;
import datetime;
import random;
import pygame;
from Bullet import Bullet;
from Wall import Wall;

def loadGameLevel(fileName, screen, settings, walls, astronautBlue, astronautOrange):
    # Open the file.
    inputFile = open(fileName, "r");

    # Read the background color.
    backgroundColor = inputFile.readline().split();
    backgroundColorRed   = int(backgroundColor[0]);
    backgroundColorGreen = int(backgroundColor[1]);
    backgroundColorBlue  = int(backgroundColor[2]);
    settings.backgroundColor = (backgroundColorRed, backgroundColorGreen, backgroundColorBlue);

    # Read the walls.
    numberOfWalls = int(inputFile.readline().split()[0]);

    for i in range(0, numberOfWalls):
        wallInfo = inputFile.readline().split();
        wallPositionX   = int(wallInfo[0]);
        wallPositionY   = int(wallInfo[1]);
        wallWidth       = int(wallInfo[2]);
        wallHeight      = int(wallInfo[3]);
        wallColorRed    = int(wallInfo[4]);
        wallColorGreen  = int(wallInfo[5]);
        wallColorBlue   = int(wallInfo[6]);
        createWall(screen, walls, wallPositionX, wallPositionY, wallWidth, wallHeight, (wallColorRed, wallColorGreen, wallColorBlue));
    
    # Read the characters' position and direction.
    astronautBlueInfo = inputFile.readline().split();
    settings.astronautBlueSpawnPositionX = int(astronautBlueInfo[0]);
    settings.astronautBlueSpawnPositionY = int(astronautBlueInfo[1]);
    astronautBlue.rect.x = settings.astronautBlueSpawnPositionX;
    astronautBlue.rect.y = settings.astronautBlueSpawnPositionY;
    astronautBlue.isLookingToTheLeft = True if int(astronautBlueInfo[2]) == 1 else False;
    if astronautBlue.isLookingToTheLeft:
        astronautBlue.flipSprites();

    astronautOrangeInfo = inputFile.readline().split();
    settings.astronautOrangeSpawnPositionX = int(astronautOrangeInfo[0]);
    settings.astronautOrangeSpawnPositionY = int(astronautOrangeInfo[1]);
    astronautOrange.rect.x = settings.astronautOrangeSpawnPositionX;
    astronautOrange.rect.y = settings.astronautOrangeSpawnPositionY;
    astronautOrange.isLookingToTheLeft = True if int(astronautOrangeInfo[2]) == 1 else False;
    if astronautOrange.isLookingToTheLeft:
        astronautOrange.flipSprites();

    # Close the file.
    inputFile.close();

def createWall(screen, walls, x, y, width, height, color):
    wall = Wall(screen, x, y, width, height, color);
    walls.add(wall);

def checkEvents(settings, screen, astronautBlue, astronautOrange, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saveScores(astronautBlue, astronautOrange);
            sys.exit();

        elif event.type == pygame.KEYDOWN:
            checkKeyDownEvents(event, settings, screen, astronautBlue, astronautOrange, bullets);
        
        elif event.type ==pygame.KEYUP:
            checkKeyUpEvents(event, settings, screen, astronautBlue, astronautOrange, bullets);

def saveScores(blueAstronaut, orangeAstronaut):
    outputFile = open("scores/scores.txt", 'a');
    outputFile.write("Total Kills: " + str(blueAstronaut.totalKills) + " - " + str(orangeAstronaut.totalKills) + '\n');
    outputFile.write("Greatest Consecutive Kills: " + str(blueAstronaut.greatestConsecutiveKills) + " - " + str(orangeAstronaut.greatestConsecutiveKills) + '\n');
    outputFile.write('\n');
    outputFile.close();

def checkKeyDownEvents(event, settings, screen, astronautBlue, astronautOrange, bullets):
        # Press ESC to exit the game.
        if event.key == pygame.K_ESCAPE:
            saveScores(astronautBlue, astronautOrange);
            sys.exit();

        # If either of the austronaut dies, press R to restart the game.
        elif event.key == pygame.K_r and (astronautBlue.health <= 0 or astronautOrange.health <= 0):
            restartGame(astronautBlue, astronautOrange, bullets);
        
        # Blue Astronaut's Controls
        if astronautBlue.health > 0:
            if event.key == pygame.K_d:
                astronautBlue.movingRight = True;
            if event.key == pygame.K_a:
                astronautBlue.movingLeft = True;
            if event.key == pygame.K_w:
                astronautBlue.movingUp = True;
            if event.key == pygame.K_s:
                astronautBlue.movingDown = True;
            if event.key == pygame.K_SPACE:
                astronautBlue.fireBullet();

        # Orange Astronaut's Controls
        if astronautOrange.health > 0:
            if event.key == pygame.K_RIGHT:
                astronautOrange.movingRight = True;
            if event.key == pygame.K_LEFT:
                astronautOrange.movingLeft = True;
            if event.key == pygame.K_UP:
                astronautOrange.movingUp = True;
            if event.key == pygame.K_DOWN:
                astronautOrange.movingDown = True;
            if event.key == pygame.K_RETURN:
                astronautOrange.fireBullet();

def restartGame(astronautBlue, astronautOrange, bullets):
    # Remove all bullets in the previous round.
    for bullet in bullets.copy():
        bullets.remove(bullet);
    
    # Reset the blue astronaut.
    if astronautBlue.isLookingToTheLeft != astronautBlue.settings.astronautBlueInitiallyLooksToTheLeft:
        astronautBlue.flipSprites();
        astronautBlue.isLookingToTheLeft = astronautBlue.settings.astronautBlueInitiallyLooksToTheLeft;
    astronautBlue.currentSprite = astronautBlue.standingSprite;
    astronautBlue.rect = astronautBlue.currentSprite.get_rect();
    astronautBlue.rect.x = astronautBlue.settings.astronautBlueSpawnPositionX;
    astronautBlue.rect.y = astronautBlue.settings.astronautBlueSpawnPositionY;   
    astronautBlue.health = astronautBlue.settings.astronautHealth;

    # Reset the orange astronaut.
    if astronautOrange.isLookingToTheLeft != astronautOrange.settings.astronautOrangeInitiallyLooksToTheLeft:
        astronautOrange.flipSprites();
        astronautOrange.isLookingToTheLeft = astronautOrange.settings.astronautOrangeInitiallyLooksToTheLeft;
    astronautOrange.currentSprite = astronautOrange.standingSprite;
    astronautOrange.rect = astronautOrange.currentSprite.get_rect();
    astronautOrange.rect.x = astronautOrange.settings.astronautOrangeSpawnPositionX;
    astronautOrange.rect.y = astronautOrange.settings.astronautOrangeSpawnPositionY; 
    astronautOrange.health = astronautOrange.settings.astronautHealth;

def checkKeyUpEvents(event, settings, screen, astronautBlue, astronautOrange, bullets):
        # Blue Astronaut's Controls
        if event.key == pygame.K_d:
            astronautBlue.movingRight = False;
        if event.key == pygame.K_a:
            astronautBlue.movingLeft = False;
        if event.key == pygame.K_w:
            astronautBlue.movingUp = False;
        if event.key == pygame.K_s:
            astronautBlue.movingDown = False;

        # Orange Astronaut's Controls
        if event.key == pygame.K_RIGHT:
            astronautOrange.movingRight = False;
        if event.key == pygame.K_LEFT:
            astronautOrange.movingLeft = False;
        if event.key == pygame.K_UP:
            astronautOrange.movingUp = False;
        if event.key == pygame.K_DOWN:
            astronautOrange.movingDown = False;

def updateAstronauts(astronautBlue, astronautOrange):
    astronautBlue.update();
    astronautOrange.update();

def updateBullets(settings, astronautBlue, astronautOrange, bullets, walls):
    bullets.update();
    for bullet in bullets.copy():

        # Check if the bullet hits the blue astronaut.
        if bullet.rect.colliderect(astronautBlue.rect) and bullet.owner != astronautBlue:
            astronautBlue.health -= bullet.damage;
            bullets.remove(bullet);
            if astronautBlue.health <= 0:       
                bullet.owner.totalKills += 1;
                bullet.owner.consecutiveKills += 1;
                if bullet.owner.consecutiveKills > bullet.owner.greatestConsecutiveKills:
                    bullet.owner.greatestConsecutiveKills = bullet.owner.consecutiveKills;

                astronautBlue.die();
                astronautBlue.consecutiveKills = 0;
        
        # Check if the bullet hits the orange astronaut.
        if bullet.rect.colliderect(astronautOrange.rect) and bullet.owner != astronautOrange:
            astronautOrange.health -= bullet.damage;
            bullets.remove(bullet);
            if astronautOrange.health <= 0:            
                bullet.owner.totalKills += 1;
                bullet.owner.consecutiveKills += 1;
                if bullet.owner.consecutiveKills > bullet.owner.greatestConsecutiveKills:
                    bullet.owner.greatestConsecutiveKills = bullet.owner.consecutiveKills;

                astronautOrange.die();
                astronautOrange.consecutiveKills = 0;

        # Remove the bullets that hit the walls.
        for wall in walls.copy():
            if bullet.rect.colliderect(wall.rect):
                bullets.remove(bullet);

        # Remove the bullets that come out of the screen.
        if bullet.rect.x > settings.screenWidth or bullet.rect.x + settings.bulletWidth < 0:
            bullets.remove(bullet);

def updateScreen(settings, screen, astronautBlue, astronautOrange, bullets, walls):
    pygame.display.set_caption("Space Battle (Blue: " + str(astronautBlue.totalKills) + ", Orange: " + str(astronautOrange.totalKills) + ")");
    screen.fill(settings.backgroundColor);

    # Draw the walls.
    for wall in walls.sprites():
        wall.drawWall();

    # Draw the bullets.
    for bullet in bullets.sprites():
        bullet.drawBullet();
    
    # Draw the astronauts.
    astronautBlue.blitMe();
    astronautOrange.blitMe();

    pygame.display.flip();