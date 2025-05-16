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
        # self.coordinates = [] # Used later to store the ships position


    def take_hit(self):
        """
        Records a hit and sinks the ship once all its segments are hit.
        """
        if not self.is_sunk:
            self.hits += 1
            if self.hits >= self.size:
                self.is_sunk = True


# Testing
if __name__ == '__main__':
        print("Ship module test:")
        print("Available ship configurations:", Ship.ALL_SHIPS)

        test_ship = Ship("Test Dinghy", 1)
        test_ship.take_hit()
        print(f"{test_ship.name} - Hits: {test_ship.hits}, Sunk: {test_ship.is_sunk}")


        if "Carrier" in Ship.ALL_SHIPS:
            carrier_size = Ship.ALL_SHIPS["Carrier"]
            carrier_test = Ship("Carrier", carrier_size)
            print(f"Created from config: {carrier_test.name}, Size: {carrier_test.size}")