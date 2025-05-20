# Heroku entry point for the Battleship game:
# imports and launches the main game loop.
from classes.game import Game

if __name__ == '__main__':
    # Instantiate the game and start the main loop
    game = Game()
    game.run_game()
