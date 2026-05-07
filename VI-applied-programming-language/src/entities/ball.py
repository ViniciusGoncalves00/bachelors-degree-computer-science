import pygame

class Ball:
    def __init__(self):
        self.radius = 10

        self.x = 400
        self.y = 300

        self.vx = 300
        self.vy = -300

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x <= self.radius or self.x >= 800 - self.radius:
            self.vx *= -1

        if self.y <= self.radius:
            self.vy *= -1

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