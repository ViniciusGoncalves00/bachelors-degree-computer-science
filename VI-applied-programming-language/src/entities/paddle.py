import pygame

class Paddle:
    def __init__(self):
        self.width = 120
        self.height = 20

        self.x = 340
        self.y = 550

        self.speed = 500

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt

        self.rect.x = max(0, min(800 - self.width, self.rect.x))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)