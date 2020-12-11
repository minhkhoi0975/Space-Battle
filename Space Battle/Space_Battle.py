# Project: Space Battle
# Author: Khoi Ho
# Description: This is a 2-player game in which each player controls a astronaut and tries to kill the other.

import sys;
import os;
import pygame;
from pygame.sprite import Group;
from Settings import Settings;
from Astronaut import Astronaut;
from Wall import Wall;
import GameFunctions;

def launchGame():

    # Show the available maps.
    availableMaps = os.listdir("levels");
    print("All available levels: ");
    for map in availableMaps:
        print("\t" + map);

    # Ask the user to enter the map they want to play.
    selectedMap = "none";
    while selectedMap not in availableMaps:
        selectedMap = input("Please enter the level you want to play: ");

    # Initialize pygame.
    pygame.init();

    # Initialize game settings.
    settings = Settings();

    # Create a window with the specified size.
    screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight));

    # Set the title of the window.
    pygame.display.set_caption("Space Battle");

    # Create an empty list of walls.
    walls = Group();

    # Create an empty list of bullets.
    bullets = Group();

    # Create astronauts.
    astronautBlue = Astronaut(settings, screen, walls, bullets, "sprites/astronaut_blue_standing.png", "sprites/astronaut_blue_dead.png");
    astronautOrange =  Astronaut(settings, screen, walls, bullets, "sprites/astronaut_orange_standing.png", "sprites/astronaut_orange_dead.png");

    # Read the game level from a file.
    GameFunctions.loadGameLevel("levels/" + selectedMap, screen, settings, walls, astronautBlue, astronautOrange);

    # Start the game loop.
    while True:
        # Limit the frame rate to 80 FPS.
        clockobject = pygame.time.Clock();
        clockobject.tick(80);

        GameFunctions.checkEvents(settings, screen, astronautBlue, astronautOrange, bullets);
        GameFunctions.updateAstronauts(astronautBlue, astronautOrange);
        GameFunctions.updateBullets(settings, astronautBlue, astronautOrange, bullets, walls);
        GameFunctions.updateScreen(settings, screen, astronautBlue, astronautOrange, bullets, walls);

launchGame();


