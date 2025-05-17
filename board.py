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

    def display_radar_view(self):
        """
        Prints the board from radar view,
        showing water (~), miss (o) and hits (x)
        """
        # Line for spacing
        print()
        header = "  " + " ".join(self.col_labels)
        print(header)

        for i in range(self.size):
            row_label = self.row_labels[i]
            row_display_elements = []
            for cell_value in self.grid[i]:
                if cell_value == 'S':
                    row_display_elements.append('~')
                else:
                    row_display_elements.append(str(cell_value))
            row_str = " ".join(row_display_elements)
            print(f"{row_label} {row_str}")
        # Line for spacing
        print()

    def place_ship(self, ship_to_place, start_row, start_col, orientation, show_error_message):
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
            if show_error_message:
                print("Error: Invalid orientation!")
            return False

        for r_coord, c_coord in coordinates:
            if not (0 <= r_coord < self.size and 0 <= c_coord < self.size):
                if show_error_message:
                    print("Error: Ship placement is outside of the playboard!")
                return False

        for r_coord, c_coord in coordinates:
            if self.grid[r_coord][c_coord] != '~':
                if show_error_message:
                    print("Error: Ship overlaps with another!")
                return False

        for r_coord, c_coord in coordinates:
            self.grid[r_coord][c_coord] = 'S'

        ship_to_place.set_coordinates(coordinates)

        return True

    def receive_shot(self, row, col):
        """
        Processes a shot at the given row and col.
        Updates the grid cell to 'x' for a hit, 'o' for a miss.
        """
        if not (0 <= row < self.size and 0 <= col < self.size):
            return None

        current_cell_value = self.grid[row][col]

        if current_cell_value == 'S':
            self.grid[row][col] = 'x'
            return "hit"
        elif current_cell_value == '~':
            self.grid[row][col] = 'o'
            return "miss"
        elif current_cell_value == 'x' or current_cell_value == 'o':
            return "already_shot"
        else:
            return None
