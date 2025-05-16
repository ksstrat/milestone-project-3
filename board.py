from ship import Ship


class Board:
    """
    Represents the 10x10 game board for Battleship.
    Manages the grid, ship placements and attacks.
    """
    def __init__(self):
        """
        Initializes a 10x10 board.
        """
        self.size = 10
        self.grid = [['~' for _ in range(self.size)] for _ in range(self.size)]
        self.row_labels = "ABCDEFGHIJ"
        self.col_labels = [str(i) for i in range(1, self.size + 1)]


    def display(self):
        """
        Prints the current state of the board to the console,
        including row and column labels.
        """
        # Line for spacing
        print()
        header = "  " + " ".join(self.col_labels)
        print(header)

        for i in range(self.size):
            row_label = self.row_labels[i]
            row_str = " ".join(str(cell) for cell in self.grid[i])
            print(f"{row_label} {row_str}")
        # Line for spacing
        print()


    def place_ship(self, ship_to_place, start_row, start_col, orientation):
        """
        Place a ship on the board if the placement is valid.
        Updates the ship's coordinates if successfully placed.
        """
        ship_size = ship_to_place.size
        coordinates = []

        if orientation.lower() == 'h':
            for i in range(ship_size):
                coordinates.append((start_row, start_col + i))
        elif orientation.lower() == 'v':
            for i in range(ship_size):
                coordinates.append((start_row + i, start_col))
        else:
            print("Error: Invalid orientation!")
            return False

        for r_coord, c_coord in coordinates:
            if not (0 <= r_coord < self.size and 0 <= c_coord < self.size):
                print("Error: Ship placement is outside of the playboard!")
                return False
            
        for r_coord, c_coord in coordinates:
            if self.grid[r_coord][c_coord] != '~':
                print("Error: Ship overlaps with another!")
                return False
        
        for r_coord, c_coord in coordinates:
            self.grid[r_coord][c_coord] = 'S'

        ship_to_place.set_coordinates(coordinates)

        return True


if __name__ == '__main__':
    test_board = Board()
    
    # Test Ship
    submarine = Ship("TestSub", 3)
    patrol = Ship("TestPatrol", 2)
    invalid_ship = Ship("TooLong", 11)  # To Long for Playboard

    print("Initial board:")
    test_board.display()

    # Test 1: valid horizontal placement
    print("\nPlacing Test Ship 1 horizontally at (0,0)...")
    if test_board.place_ship(submarine, 0, 0, 'H'):
        print("Test Ship 1 placed successfully.")
        print(f"Test Ship 1 coordinates: {submarine.coordinates}")
    else:
        print("Failed to place Test Ship 1.")
    test_board.display()

    # Test 2: valid vertical placement
    print("\nPlacing Test Ship 2 vertically at (2,2)...")
    if test_board.place_ship(patrol, 2, 2, 'V'):
        print("Test Ship 2 placed successfully.")
        print(f"Test Ship 2 coordinates: {patrol.coordinates}")
    else:
        print("Failed to place Test Ship 2.")
    test_board.display()

    # Test 3: Invalid horizontal placement
    print("\nTrying to place Test Ship horizontally at (0,8)... (should fail)")
    submarine_test_fail = Ship("SubmarineFail", 3) 
    if test_board.place_ship(submarine_test_fail, 0, 8, 'H'):  # 0,8 ; 0,9 ; 0,10 (out)
        print("SubmarineFail placed successfully (ERROR - SHOULD FAIL).")
    else:
        print("Failed to place SubmarineFail as expected.")
    test_board.display()

    # Test 4: invalid vertical placement
    print("\nTrying to place TestPatrol vertically at (9,0)... (should fail)")
    patrol_test_fail = Ship("PatrolFail", 2)
    if test_board.place_ship(patrol_test_fail, 9, 0, 'V'):  # 9,0 ; 10,0 (out)
        print("PatrolFail placed successfully (ERROR - SHOULD FAIL).")
    else:
        print("Failed to place PatrolFail as expected.")
    test_board.display()

    # Test 5: invalid orientation
    print("\nTrying to place TestPatrol with invalid orientation 'X'...")
    patrol_orient_fail = Ship("PatrolOrientFail", 2)
    if test_board.place_ship(patrol_orient_fail, 5, 5, 'X'):
        print("PatrolOrientFail placed successfully (ERROR - SHOULD FAIL).")
    else:
        print("Failed to place PatrolOrientFail due to invalid orientation.")
    test_board.display()

    # Board restet for overlapping test)
    print("\n--- Testing Overlap ---")
    initial_board_overlap_test = Board()  # New Playboard for overlapping test
    ship_alpha = Ship("Alpha", 3)
    print("Placing Ship Alpha at (1,1) horizontally...")
    initial_board_overlap_test.place_ship(ship_alpha, 1, 1, 'h')  # (1,1), (1,2), (1,3)
    initial_board_overlap_test.display()

    # Test 6: Try to Overlap
    print("\nTrying to place Ship Bravo at (1,2) horizontally (should overlap Alpha and fail)...")
    ship_bravo_overlap = Ship("BravoOverlap", 3)
    if initial_board_overlap_test.place_ship(ship_bravo_overlap, 1, 2, 'h'):  # (1,2), (1,3), (1,4)
        print("Ship BravoOverlap placed (ERROR - SHOULD HAVE FAILED DUE TO OVERLAP).")
    else:
        print("Failed to place Ship BravoOverlap as expected (overlap).")
    initial_board_overlap_test.display()

    # Test 7: Try to set ship on another coordinate
    print("\nPlacing Ship Charlie at (3,3) vertically (should succeed)...")
    ship_charlie_valid = Ship("CharlieValid", 2)
    if initial_board_overlap_test.place_ship(ship_charlie_valid, 3, 3, 'v'):
        print("Ship CharlieValid placed successfully.")
    else:
        print("Failed to place Ship CharlieValid (UNEXPECTED FAILURE).")
    initial_board_overlap_test.display()