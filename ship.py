class Ship:
    """
    Represents the ships in the game.
    Keeps track of size, hits and determines when the ship has been sunk.
    """

    ALL_SHIPS = {
        "Carrier": 5,
        "Battleship": 4,
        "Destroyer": 3,
        "Submarine": 3,
        "Patrol Boat": 2
    }


    def __init__(self, name, size):
        """
        Initializing new ship.
        """
        self.name = name
        self.size = size
        self.hits = 0
        self.is_sunk = False
        self.coordinates = []


    def take_hit(self):
        """
        Records a hit and sinks the ship once all its segments are hit.
        """
        if not self.is_sunk:
            self.hits += 1
            if self.hits >= self.size:
                self.is_sunk = True

    def set_coordinates(self, new_coordinates):
        """
        Sets the ship's coordinates.
        """
        self.coordinates = new_coordinates