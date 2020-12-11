import sys;
import pygame;
from pygame.sprite import Group;
from Settings import Settings;
from Astronaut import Astronaut;
from Wall import Wall;
import GameFunctions;

def launchGame():

    # Initialize pygame.
    pygame.init();

    # Initialize game settings.
    settings = Settings();

    # Create a window with the specified size.
    screen = pygame.display.set_mode((settings.width, settings.height));

    # Set the title of the window.
    pygame.display.set_caption("Space Battle");

    # Create walls.
    walls = Group();
    GameFunctions.createWall(screen, walls, settings.width / 2 - 50, 100, 100, 300, (255, 255, 255));

    # Create an astronaut.
    astronaut = Astronaut(settings, screen, walls);

    # Create a bullet list.
    bullets = Group();

    # Start the game loop.
    while True:
        GameFunctions.checkEvents(settings, screen, astronaut, bullets);
        GameFunctions.updateAstronaut(astronaut, walls);
        GameFunctions.updateBullets(settings, bullets);
        GameFunctions.updateScreen(settings, screen, astronaut, bullets, walls);

launchGame();

