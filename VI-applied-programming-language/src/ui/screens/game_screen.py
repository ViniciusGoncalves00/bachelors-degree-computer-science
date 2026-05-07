import pygame
from src.ui.screens.screen import Screen
from src.entities.ball import Ball
from src.entities.brick import Brick
from src.entities.paddle import Paddle

class GameScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

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
        pass

    def update(self, dt):
        self.paddle.update(dt)
        self.ball.update(dt)

        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.vy *= -1
            self.ball.y = self.paddle.rect.top - self.ball.radius

        for brick in self.bricks:
            if brick.alive and self.ball.rect.colliderect(brick.rect):
                brick.alive = False
                self.ball.vy *= -1
                break

    def draw(self, surface):
        surface.fill((20, 20, 30))

        self.paddle.draw(surface)
        self.ball.draw(surface)

        for brick in self.bricks:
            brick.draw(surface)