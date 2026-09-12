import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PyGame Project")

        self.clock = pygame.time.Clock()
        self.running = True

        self.current_screen = None

    def set_screen(self, screen):
        self.current_screen = screen

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.current_screen.handle_event(event)

            self.current_screen.update(dt)
            self.current_screen.draw(self.screen)

            pygame.display.flip()

        pygame.quit()