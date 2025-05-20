from board import Board
from ship import Ship
from board import Colors
import random
import time


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

        self.current_player = "player"

    def _display_boards_side_by_side(self):
        """
        Displays the player's board and the computer's radar view side-by-side.
        Utilizes the get_display_elements() method from the Board class.
        """
        player_board_title = "OUR STATUS"
        computer_board_title = "RADAR VIEW"

        col_numbers_str = " ".join(self.player_board.col_labels)
        col_numbers_width = len(col_numbers_str)

        single_board_display_width = 2 + col_numbers_width

        spacing_between_boards = " " * 25

        print(f"\n{Colors.grey_color}---! Captain {self.player_name}'s Turn !{Colors.default_color}---")
        print()

        print(f"{player_board_title.center(single_board_display_width)}{spacing_between_boards}{computer_board_title.center(single_board_display_width)}")

        col_header_segment_str = " " + col_numbers_str
        print(f"{col_header_segment_str}{spacing_between_boards}{col_header_segment_str}")

        for i in range(self.player_board.size):
            row_label = self.player_board.row_labels[i]

            player_row_elements = self.player_board.get_display_elements(i, for_radar_view=False)
            computer_row_elements = self.computer_board.get_display_elements(i, for_radar_view=True)

            player_row_data_str = " ".join(player_row_elements)
            computer_row_data_str = " ".join(computer_row_elements)

            print(f"{row_label} {player_row_data_str.ljust(col_numbers_width)}{spacing_between_boards}{row_label} {computer_row_data_str.ljust(col_numbers_width)}")
        print()

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

    def _parse_coordinate_input(self, coord_str):
        """
        Parses a string like "A5" into (row, col) tuple.
        Returns None if input is invalid.
        """
        coord_str = coord_str.strip().upper()
        if not (2 <= len(coord_str) <= 3):
            return None

        row_char = coord_str[0]
        col_str = coord_str[1:]

        if not row_char.isalpha() or not col_str.isdigit():
            return None

        if row_char not in self.player_board.row_labels:
            return None
        row_index = self.player_board.row_labels.find(row_char)

        try:
            col_num = int(col_str)
            if not (1 <= col_num <= self.player_board.size):
                return None
            col_index = col_num - 1
        except ValueError:
            return None

        return (row_index, col_index)

    def _manually_place_ship(self, ship_to_place):
        """
        Handles the input process for manually placing a ship.
        Focuses on getting and validating input.
        """
        print(f"\nCommand your {ship_to_place.name} (Size: {ship_to_place.size}).")

        placed_on_board_successfully = False
        while not placed_on_board_successfully:
            print("Current state:")
            self.player_board.display()

            start_row, start_col, orientation_input = -1, -1, ''

            while True:
                coord_input = input(f"Command us start coordinate (e.g., A1, J10) for our {ship_to_place.name}: ").strip()
                if not coord_input:
                    print("We need coordinates! Ready to receive new orders.")
                    continue
                parsed_coords = self._parse_coordinate_input(coord_input)
                if parsed_coords:
                    start_row, start_col = parsed_coords
                    break
                else:
                    print("We can't execute this manoeuvre captain! Please command us a letter (A-J) followed by a number (1-10).")

            while True:
                orientation_input = input(f"Command us orientation for our {ship_to_place.name} (h for horizontal, v for vertical): ").strip().lower()
                if orientation_input in ['h', 'v']:
                    break
                else:
                    print("We can't execute this manoeuvre captain! Please command us 'h' or 'v'.")

            placed_on_board_successfully = self.player_board.place_ship(
                ship_to_place, start_row, start_col, orientation_input, show_error_message=True
            )

            if placed_on_board_successfully:
                print(f"{ship_to_place.name} has received command!")
                time.sleep(1.5)
            else:
                print("We can't execute this manoeuvre captain! Ready to receive new orders")
                time.sleep(1.5)

    def _computer_take_shot(self):
        """
        Handles the computer's turn to take a shot.
        Chooses a random coordinate on the player's board.
        Processes the shot and provides feedback.
        """
        print(f"\n{Colors.red_color}---! Enemy's Turn !---{Colors.default_color}")
        print()
        time.sleep(1)
        board_size = self.player_board.size
        valid_shot_found = False
        shot_row, shot_col = -1, -1

        while not valid_shot_found:
            shot_row = random.randint(0, board_size - 1)
            shot_col = random.randint(0, board_size - 1)
            if self.player_board.grid[shot_row][shot_col] not in ['x', 'o']:
                valid_shot_found = True

        coord_display_str = f"{self.player_board.row_labels[shot_row]}{self.player_board.col_labels[shot_col]}"
        print(f"Enemy fires at {coord_display_str}...")
        time.sleep(1.5)

        shot_result_on_grid = self.player_board.receive_shot(shot_row, shot_col)

        if shot_result_on_grid == "hit":
            print("> Enemy HIT your ship! <")
            time.sleep(1.5)
            for player_ship in self.player_fleet:
                if (shot_row, shot_col) in player_ship.coordinates:
                    player_ship.take_hit()
                    if player_ship.is_sunk:
                        print(f"!!! Enemy sank your {player_ship.name} !!!")
                        time.sleep(1.5)
                    break
        elif shot_result_on_grid == "miss":
            print("> Enemy MISSED! <")
            time.sleep(1.5)

    def _all_ships_sunk(self, fleet):
        """
        Checks if all ships in the given fleet are sunk.
        """
        for ship in fleet:
            if not ship.is_sunk:
                return False
        return True

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
                print(f"Welcome, Captain {self.player_name}!")
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
        print("6. A hit on a ship is marked 'x'.")
        print("7. A miss (shot into water) is marked 'o'.")
        print("8. The first player to sink all of the opponent's ships wins.")
        print("--- End of Rules ---")
        input("\nPress Enter to return to the menu...")

    def _get_player_shot_coordinate(self):
        """
        Prompts the player for a shot coordinate.
        Checks if the coordinate has already been targeted.
        """
        while True:
            coord_input = input(f"\nCaptain {self.player_name}, where should we shoot? We need coordinates! (e.g., B6)\n")
            if not coord_input:
                print("Invalid input. Please try again.")
                continue

            parsed_coords = self._parse_coordinate_input(coord_input)
            if parsed_coords:
                row, col = parsed_coords
                if self.computer_board.grid[row][col] == 'x' or self.computer_board.grid[row][col] == 'o':
                    print("We have already fired at this coordinate! Please try again.")
                    continue
                else:
                    return parsed_coords
            else:
                print("Invalid input. Please use a letter (A-J) followed by a number (1-10).")

    def run_game(self):
        """
        Main method to manage the overall game flow.
        Starts with the main menu and proceeds to game setup and play if chosen by the player.
        The game loop allows the layer to take one shot before currently ending.
        """
        while True:
            menu_choice = self.show_start_screen()

            if menu_choice == 'q':
                print("Thanks for playing Battleship! Have a nice day!")
                break

            elif menu_choice == 'r':
                self.show_rules()
                continue

            elif menu_choice == "s":
                self.player_board = Board()
                self.computer_board = Board()
                self.player_fleet = []
                self.computer_fleet = []
                for name, size in Ship.ALL_SHIPS.items():
                    self.player_fleet.append(Ship(name, size))
                    self.computer_fleet.append(Ship(name, size))

                self._setup_computer_board()
                self.current_player = "player"

                self.get_player_name()
                self.get_ship_placement_choice()

                print("\nOur ships prepare for depature...")
                if self.ship_placement_method == "random":
                    print("\nOur ships will spread without a strategy...\n")
                    self._place_ships_randomly(self.player_fleet, self.player_board)
                    print("Our ships have taken up random positions!")
                    print("\nThis is our nautical chart:")
                    self.player_board.display()
                else:
                    print("\n--- Decide Ship Positioning ---")
                    for player_ship in self.player_fleet:
                        self._manually_place_ship(player_ship)
                    print("\nAll ships in position!")
                    print("This is our nautical chart:")
                    self.player_board.display()

                print(f"\n{Colors.red_color}---! Enemy's in Range !---{Colors.default_color}")
                time.sleep(1)
                game_is_running = True

                while game_is_running:
                    if self.current_player == "player":
                        self._display_boards_side_by_side()

                        shot_coords = self._get_player_shot_coordinate()
                        r, c = shot_coords
                        coord_display_str = f"{self.player_board.row_labels[r]}{self.player_board.col_labels[c]}"
                        print(f"\nCaptain {self.player_name} fires at {coord_display_str}...")
                        time.sleep(1.5)

                        shot_result_on_grid = self.computer_board.receive_shot(r, c)
                        if shot_result_on_grid == "hit":
                            print("> HIT! <")
                            time.sleep(1.5)
                            for comp_ship in self.computer_fleet:
                                if (r, c) in comp_ship.coordinates:
                                    comp_ship.take_hit()
                                    if comp_ship.is_sunk:
                                        print(f"! Enemy {comp_ship.name} has been sunk !")
                                        time.sleep(1.5)
                                    break
                        elif shot_result_on_grid == "miss":
                            print("> MISS! <")
                            time.sleep(1.5)

                        if self._all_ships_sunk(self.computer_fleet):
                            print(f"\n! We have won the battle, Captain {self.player_name}! YOU WIN! !")
                            print("You have sunk all enemy ships!")
                            time.sleep(1)
                            print("Final chart:")
                            self.computer_board.display()
                            game_is_running = False

                        if game_is_running:
                            self.current_player = "computer"

                    elif self.current_player == "computer":
                        self._computer_take_shot()

                        if self._all_ships_sunk(self.player_fleet):
                            print("\n! OUR FLEET IS GONE! The enemy wins this battle. !")
                            time.sleep(1)
                            print("Final chart:")
                            self.player_board.display()
                            game_is_running = False

                        if game_is_running:
                            self.current_player = "player"

                print("\n--- Game Over ---")
                continue


# Main Game execution
if __name__ == '__main__':
    game = Game()
    game.run_game()
