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


if __name__ == '__main__':
    test_board = Board()
    print("Board module test - display method:")
    test_board.display()