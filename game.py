from board import Board
from ship import Ship
import random

class Game:
    """
    Manages the overall Battleship game flow, including setup, turns, and game state.
    """
    def __init__(self):
        """
        Initializes the game
        """
        self.player_name = "Player"
        self.ship_placement_method = "random"

        self.player_board = Board()
        self.computer_board = Board()

        self.player_fleet = []
        self.computer_fleet = []

        for name, size in Ship.ALL_SHIPS.items():
            self.player_fleet.append(Ship(name, size))
            self.computer_fleet.append(Ship(name, size))

        self._setup_computer_board()


    def _place_ships_randomly(self, fleet_to_place, target_board):
        """
        Places all ship from the given fleet randomly on the target board.
        Ensures ships are placed according to board rules.
        """
        board_size = target_board.size

        for ship in fleet_to_place:
            placed_successfully = False
            while not placed_successfully:
                orientation = random.choice(['h', 'v'])

                if orientation == 'h':
                    max_col = board_size - ship.size
                    start_row = random.randint(0, board_size - 1)
                    start_col = random.randint(0, max_col if max_col >= 0 else 0)
                else:
                    max_row = board_size - ship.size
                    start_row = random.randint(0, max_row if max_row >= 0 else 0)
                    start_col = random.randint(0, board_size - 1)

                placed_successfully = target_board.place_ship(ship, start_row, start_col, orientation)


    def _setup_computer_board(self):
        """
        Sets up the computer's board by placing its ships randomly
        """
        self._place_ships_randomly(self.computer_fleet, self.computer_board)
        print("Enemy ships are in range!")


    def show_start_screen(self):
        """
        Displays the start screen and gets the user's initial choice.
        """
        print("########################")
        print("       Battleship       ")
        print("########################")
        print("\n Welcome to Battleship!")
        print("Choose an option:")
        print(" (s) Start Game")
        print(" (r) See the Rules")
        print(" (q) Quit")

        while True:
            choice = input("Enter your choice (s/r/q): ").lower()
            if choice in ['s', 'r', 'q']:
                return choice
            else:
                print("Invalid choice. Please enter 's', 'r', or 'q'.")


    def get_player_name(self):
        """
        Prompts the user to enter their name.
        """
        while True:
            name = input("Enter your name: ")
            if name.strip():
                self.player_name = name
                print(f"Welcome, {self.player_name}!")
                break
            else:
                print("Name cannot be empty. Please enter your name.")

    def get_ship_placement_choice(self):
        """
        Asks the player how they want to place their ships.
        """
        print("\nShip Placement:")
        print(" (m) Manually place your ships")
        print(" (r) Randomly place your ships")

        while True:
            choice = input("Choose ship placement method (m/r): ").lower()
            if choice == 'm':
                self.ship_placement_method = "manual"
                print("You will place your ships manually!")
                break
            elif choice == 'r':
                self.ship_placement_method = "random"
                print("Ships will be placed randomly.")
                break
            else:
                print("Invalid choice. Please enter 'm' or 'r'.")

    def show_rules(self):
        """
        Displays the game rules.
        """
        print("\n--- Game Rules ---")
        print("1. This is a 1-player game against the computer.")
        print("2. The game is played on a 10x10 grid.")
        print("3. Each player has a fleet of 5 ships of different sizes:")
        for name, size in Ship.ALL_SHIPS.items():
            print(f" - {name} ({size} squares)")
        print("4. Ships can be placed horizontally or vertically, but can not overlap.")
        print("5. Players take turns guessing coordinates to hit enemy ships.")
        print("6. A hit is marked 'H' (on your tracking grid) or 'X' (on your own ship).")
        print("7. A miss is marked 'M' (on your tracking grid) or 'O' (opponent's miss on your water).")
        print("8. The first player to sink all of the opponent's ships wins.")
        print("--- End of Rules ---")
        input("\nPress Enter to return to the menu...")

    def run_game(self):
        """
        Main method to run the game.
        """
        while True:
            choice = self.show_start_screen()

            if choice == 's':
                self.get_player_name()
                self.get_ship_placement_choice()
                print("\nStarting game setup...")
                print(f"Game will start for {self.player_name} with {self.ship_placement_method} placement.")

                # Testprint
                print(f"Player board size: {self.player_board.size}x{self.player_board.size}")

                if self.ship_placement_method == "random":
                    print("Placing ships randomly...")
                    self._place_ships_randomly(self.player_fleet, self.player_board)
                    print("Your ships have been placed randomly.")
                    print("\nThis is your board:")
                    self.player_board.display()
                else:
                    print("\nManual ship placement selected.")
                    # Implement manual placement pending
                    print("Your board:")
                    self.player_board.display()

                # Implement main game loop pending
                break
            elif choice == 'r':
                self.show_rules()
            elif choice == 'q':
                print("Thanks for playing Battleship! Goodbye.")
                break


# Main Game execution
if __name__ == '__main__':
    game = Game()
    game.run_game()