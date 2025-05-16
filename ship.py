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


# Testing
if __name__ == '__main__':
        print("Ship module test:")
        print("Available ship configurations:", Ship.ALL_SHIPS)

        # Test Coordinates
        test_ship = Ship("Test Ship", 3)
        print(f"Ship created: {test_ship.name}, Size: {test_ship.size}, Coordinates: {test_ship.coordinates}")

        test_coords = [(0, 0), (0, 1), (0, 2)]
        test_ship.set_coordinates(test_coords)
        print(f"After set coords: {test_ship.name}, Coords: {test_ship.coordinates}")

        test_ship.take_hit()
        print(f"{test_ship.name} - Hits: {test_ship.hits}, Sunk: {test_ship.is_sunk}")