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