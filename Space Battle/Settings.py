class Settings():
    """description of class"""
    def __init__(self):

        # Screen settings
        self.screenWidth      = 1280;                         # Screen width
        self.screenHeight     = 640;                          # Screen height
        self.backgroundColor  = (0, 0, 0);                    # Background color. Can be changed when a game level is loaded.

        # Settings applied to both astronauts.
        self.astronautSpeedX  = 10;                           # The horizontal speed of each astronaut.
        self.astronautSpeedY  = 20;                           # The vertical speed of each astronaut.
        self.astronautGravity = 10;                           # The gravity applied to each astronaut.
        self.astronautHealth  = 100;                          # The health of each astronaut.

        # Settings applied to the blue astronaut.
        self.astronautBlueSpawnPositionX = 0;                # The x position where the blue astronaut is spawned. Can be changed when a game level is loaded.
        self.astronautBlueSpawnPositionY = 600;              # The y position where the blue astronaut is spawned. Can be changed when a game level is loaded.
        self.astronautBlueInitiallyLooksToTheLeft = False;   # Does the blue astronaut initially look to the left? Can be changed when a game level is loaded.

        # Settings applied to the orange astronaut.
        self.astronautOrangeSpawnPositionX = 1200;           # The x position where the orange astronaut is spawned. Can be changed when a game level is loaded.
        self.astronautOrangeSpawnPositionY = 600;            # The y position where the orange astronaut is spawned. Can be changed when a game level is loaded.
        self.astronautOrangeInitiallyLooksToTheLeft = True;  # Does the orange astronaut initially look to the left? Can be changed when a game level is loaded.

        # Bullet settings
        self.bulletSpeed           = 30;                     # The speed of the bullet.
        self.bulletWidth           = 15;                     # The width of the bullet.
        self.bulletHeight          = 3;                      # The height of the bullet.
        self.bulletColor           = (191, 255, 0);          # The color of the bullet.
        self.bulletBaseDamage      = 30;
        self.bulletDamageDeviation = 10;                     # The damage of a bullet is between (base damage - deviation) and (base damage + deviation).


