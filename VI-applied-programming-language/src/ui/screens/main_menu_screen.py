import pygame
from src.ui.screens.screen import Screen
from src.ui.screens.game_screen import GameScreen
from src.ui.components.button import Button

class MainMenuScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.font = pygame.font.SysFont(None, 40)

        self.start_button = Button(
            rect=(300, 250, 200, 60),
            text="Start",
            callback=self.start_game,
            font=self.font
        )

    def start_game(self):
        self.game.set_screen(GameScreen(self.game))

    def handle_event(self, event):
        self.start_button.handle_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((20, 20, 20))
        self.start_button.draw(surface)