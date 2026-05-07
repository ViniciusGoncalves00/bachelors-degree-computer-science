import pygame

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 80, 30)
        self.alive = True

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, (200, 50, 50), self.rect)