import pygame
import math

class Ball:
    def __init__(self):
        self.radius = 10

        self.x = 400
        self.y = 300

        self.speed = 400

        self.vx = 0
        self.vy = -self.speed

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x <= self.radius:
            self.x = self.radius
            self.vx *= -1

        if self.x >= 800 - self.radius:
            self.x = 800 - self.radius
            self.vx *= -1

        if self.y <= self.radius:
            self.y = self.radius
            self.vy *= -1

    def bounce_from_paddle(self, paddle):
        paddle_center = paddle.rect.centerx

        relative_intersection = (
            self.x - paddle_center
        ) / (paddle.width / 2)

        relative_intersection = max(
            -1,
            min(1, relative_intersection)
        )

        max_bounce_angle = math.radians(60)

        bounce_angle = (
            relative_intersection * max_bounce_angle
        )

        self.vx = self.speed * math.sin(bounce_angle)
        self.vy = -self.speed * math.cos(bounce_angle)

        self.y = paddle.rect.top - self.radius

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            self.radius
        )

    @property
    def rect(self):
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            self.radius * 2,
            self.radius * 2
        )