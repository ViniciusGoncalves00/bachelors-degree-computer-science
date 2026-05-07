import pygame
from src.ui.screens.screen import Screen
from src.entities.ball import Ball
from src.entities.brick import Brick
from src.entities.paddle import Paddle

PLAYING = "playing"
VICTORY = "victory"
GAME_OVER = "game_over"

class GameScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        
        self.state = PLAYING

        self.font = pygame.font.SysFont(None, 64)
        self.small_font = pygame.font.SysFont(None, 32)

        self.paddle = Paddle()
        self.ball = Ball()

        self.bricks = []

        for row in range(5):
            for col in range(8):
                brick = Brick(
                    60 + col * 85,
                    50 + row * 35
                )

                self.bricks.append(brick)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.restart()

    def update(self, dt):
        if self.state != PLAYING:
            return

        self.paddle.update(dt)
        self.ball.update(dt)
        
        if self.ball.y > 600:
            self.state = GAME_OVER
            
        remaining_bricks = [
            brick for brick in self.bricks
            if brick.alive
        ]

        if len(remaining_bricks) == 0:
            self.state = VICTORY

        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.bounce_from_paddle(self.paddle)
            self.ball.y = self.paddle.rect.top - self.ball.radius

        for brick in self.bricks:
            if brick.alive and self.ball.rect.colliderect(brick.rect):
                brick.alive = False
                self.ball.vy *= -1
                break
            
    def restart(self):
        self.__init__(self.game)

    def draw(self, surface):
        surface.fill((20, 20, 30))

        self.paddle.draw(surface)
        self.ball.draw(surface)

        for brick in self.bricks:
            brick.draw(surface)
            
        if self.state == VICTORY:
            text = self.font.render(
                "YOU WIN!",
                True,
                (0, 255, 0)
            )

            restart = self.small_font.render(
                "Press R to restart",
                True,
                (255, 255, 255)
            )

            surface.blit(text, (260, 250))
            surface.blit(restart, (280, 320))

        elif self.state == GAME_OVER:
            text = self.font.render(
                "GAME OVER",
                True,
                (255, 50, 50)
            )
        
            restart = self.small_font.render(
                "Press R to restart",
                True,
                (255, 255, 255)
            )
        
            surface.blit(text, (220, 250))
            surface.blit(restart, (280, 320))