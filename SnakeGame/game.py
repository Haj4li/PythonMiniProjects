import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.snake = Snake(width // 2, height // 2)
        self.food = Food(width, height)
        self.score = 0
        self.font = pygame.font.SysFont(None, 30)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.snake.change_direction("right")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("left")
                elif event.key == pygame.K_UP:
                    self.snake.change_direction("up")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("down")

    def update(self):
        self.snake.move()
        rect1 = pygame.Rect(self.snake.body[0][0], self.snake.body[0][1], 10,10)
        rect2 = pygame.Rect(self.food.position[0], self.food.position[1], 10,10)
        if rect1.colliderect(rect2):
            self.snake.grow()
            self.food.respawn(self.width, self.height)
            self.score += self.food.score

    def draw(self):
        self.screen.fill((0, 0, 0))
        for body_part in self.snake.body:
            pygame.draw.rect(self.screen, (255, 255, 255), (body_part[0], body_part[1], 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.food.position[0], self.food.position[1], 10, 10))
        score_text = self.font.render("Score: {}".format(self.score), True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.update()

    def check_collisions(self):
        if self.snake.body[0][0] < 0 or self.snake.body[0][0] > self.width - 10 or self.snake.body[0][1] < 0 or self.snake.body[0][1] > self.height - 10:
            self.game_over()
        # for body_part in self.snake.body[1:]:
        #     if self.snake.body[0] == body_part:
        #         self.game_over()

    def game_over(self):
        self.running = False
        game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(game_over_text, (self.width // 2 - 50, self.height // 2 - 15))
        pygame.display.update()
        pygame.time.wait(2000)

    def run(self):
        self.running = True
        while self.running:
            self.handle_input()
            self.update()
            self.draw()
            self.check_collisions()
            self.clock.tick(30)
        pygame.quit()
