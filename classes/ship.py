class Ship:
    """
    Represents the ships in the game, tracking its name, size,
    number of hits taken, sunk status, and the grid coordinates it occupies.
    """
    #  Predefined ship types with their corresponding sizes
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
        Defines name, number of hits required to sink, hit count,
        sunk status and coordinates on grid of the ship.
        """
        self.name = name
        self.size = size
        self.hits = 0
        self.is_sunk = False
        self.coordinates = []

    def take_hit(self):
        """
        Records a hit and sinks the ship once all its segments are hit.
        Increments the hit counter. Once the total hits reach the ships size,
        ship will be marked as sunk.
        """
        if not self.is_sunk:
            self.hits += 1
            if self.hits >= self.size:
                self.is_sunk = True

    def set_coordinates(self, new_coordinates):
        """
        Sets the ship's coordinates for the grid.
        """
        self.coordinates = new_coordinates
