from src.game import Game
from src.ui.screens.main_menu_screen import MainMenuScreen


if __name__ == "__main__":
    game = Game()
    game.set_screen(MainMenuScreen(game))
    game.run()