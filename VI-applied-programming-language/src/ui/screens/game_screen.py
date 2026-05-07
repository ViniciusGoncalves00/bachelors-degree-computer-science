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
                
        self.total_bricks = len(self.bricks)
        self.start_time = pygame.time.get_ticks()
        self.end_time = None

        self.paddle_hits = 0
        
        self.brick_combo = 0
        self.max_brick_combo = 0
        
        self.last_paddle_touch_time = self.start_time
        self.max_time_without_paddle = 0
        

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
            current_time = pygame.time.get_ticks()

            final_interval = (
                current_time - self.last_paddle_touch_time
            ) / 1000

            self.max_time_without_paddle = max(
                self.max_time_without_paddle,
                final_interval
            )

            self.end_time = pygame.time.get_ticks()
            self.state = GAME_OVER
            
        remaining_bricks = [
            brick for brick in self.bricks
            if brick.alive
        ]

        if len(remaining_bricks) == 0:
            current_time = pygame.time.get_ticks()

            final_interval = (
                current_time - self.last_paddle_touch_time
            ) / 1000
            
            self.max_time_without_paddle = max(
                self.max_time_without_paddle,
                final_interval
            )
            
            self.end_time = pygame.time.get_ticks()
            self.state = VICTORY

        if self.ball.rect.colliderect(self.paddle.rect):
            current_time = pygame.time.get_ticks()

            time_without_paddle = (
                current_time - self.last_paddle_touch_time
            ) / 1000

            self.max_time_without_paddle = max(
                self.max_time_without_paddle,
                time_without_paddle
            )

            self.last_paddle_touch_time = current_time

            self.paddle_hits += 1

            self.brick_combo = 0

            self.ball.bounce_from_paddle(self.paddle)

            self.ball.y = (
                self.paddle.rect.top
                - self.ball.radius
            )

        for brick in self.bricks:
            if brick.alive and self.ball.rect.colliderect(brick.rect):
                brick.alive = False

                self.brick_combo += 1

                self.max_brick_combo = max(
                    self.max_brick_combo,
                    self.brick_combo
                )

                self.ball.vy *= -1
                break
            
    def restart(self):
        self.__init__(self.game)
        
    def calculate_score(self):
        remaining = self.get_remaining_bricks()
        destroyed = self.total_bricks - remaining
        duration = self.get_match_duration()

        score = (
            destroyed * 1000
            - duration * 10
        )

        return max(0, int(score))
    
    def get_match_duration(self):
        end_time = (
            self.end_time
            if self.end_time is not None
            else pygame.time.get_ticks()
        )
    
        return (
            end_time - self.start_time
        ) / 1000
        
    def get_remaining_bricks(self):
        return len([
            brick for brick in self.bricks
            if brick.alive
        ])

    def draw(self, surface):
        surface.fill((20, 20, 30))

        self.paddle.draw(surface)
        self.ball.draw(surface)

        for brick in self.bricks:
            brick.draw(surface)
            
        if self.state in [VICTORY, GAME_OVER]:
            title = "YOU WIN!" if self.state == VICTORY else "GAME OVER"

            color = (
                (0, 255, 0)
                if self.state == VICTORY
                else (255, 50, 50)
            )

            title_text = self.font.render(
                title,
                True,
                color
            )

            surface.blit(title_text, (220, 180))

            stats = [
                f"Remaining bricks: {self.get_remaining_bricks()}",
                f"Total match time: {self.get_match_duration():.2f}s",
                f"Longest without paddle touch: {self.max_time_without_paddle:.2f}s",
                f"Best brick combo: {self.max_brick_combo}",
                f"Paddle touches: {self.paddle_hits}",
                f"Final score: {self.calculate_score()}",
            ]

            for i, stat in enumerate(stats):
            
                text = self.small_font.render(
                    stat,
                    True,
                    (255, 255, 255)
                )

                surface.blit(
                    text,
                    (170, 280 + i * 35)
                )

            restart_text = self.small_font.render(
                "Press R to restart",
                True,
                (200, 200, 200)
            )

            surface.blit(restart_text, (260, 520))