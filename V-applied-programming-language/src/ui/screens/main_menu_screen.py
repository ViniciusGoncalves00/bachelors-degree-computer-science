import pygame
from src.ui.screens.screen import Screen
from src.ui.screens.game_screen import GameScreen
from src.ui.components.button import Button

class MainMenuScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

        self.title_font = pygame.font.SysFont(None, 72)
        self.font = pygame.font.SysFont(None, 40)
        self.small_font = pygame.font.SysFont(None, 28)

        self.start_button = Button(
            rect=(300, 220, 200, 60),
            text="Start Game",
            callback=self.start_game,
            font=self.font
        )
        
        self.commands = [
            "Controls:",
            "LEFT ARROW  - Move left",
            "RIGHT ARROW - Move right",
            "R - Restart after match ends",
        ]

    def start_game(self):
        self.game.set_screen(GameScreen(self.game))

    def handle_event(self, event):
        self.start_button.handle_event(event)

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((20, 20, 30))

        title = self.title_font.render(
            "BREAKOUT",
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(center=(400, 120))

        surface.blit(title, title_rect)

        self.start_button.draw(surface)

        for i, command in enumerate(self.commands):

            text = self.small_font.render(
                command,
                True,
                (200, 200, 200)
            )

            surface.blit(
                text,
                (220, 340 + i * 35)
            )