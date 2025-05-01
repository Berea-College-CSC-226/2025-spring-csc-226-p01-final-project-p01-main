import pygame
import tkinter as tk
import tkinter.font as tkfont
import random
import time


class Game:
    def __init__(self):
        self.size = 800, 600
        self.width = 800
        self.height = 600
        self.bottom = 600
        self.top = -25
        self.left = 800
        self.right = 1600
        self.grid = 25
        self.grid_width = self.width // self.grid
        self.grid_height = self.height // self.grid
        self.score = 0
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.get_buffer()
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.size, game=self)

        self.apple = Apple(self)

    def run(self):
        while self.running:
            if (self.snake.rect.x, self.snake.rect.y) == self.apple.position:
                self.snake.length += 1
                self.apple = Apple(self)
            if self.snake.rect.x == self.left:
                self.running = False
            if self.snake.rect.y == self.bottom:
                self.running = False
            if self.snake.rect.x == self.right:
                self.running = False
            if self.snake.rect.y == self.top:
                self.running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            print(self.snake.rect.x, self.snake.rect.y)

            self.snake.movement(pygame.key.get_pressed())
            self.screen.fill('#FFFFFF')
            self.apple.drawApple(self.screen)
            self.screen.blit(self.snake.surf, self.snake.rect, )
            pygame.display.update()
            self.clock.tick(10)

        pygame.quit()


class Apple:
    def __init__(self, game):
        self.gridW = game.grid_width
        self.gridH = game.grid_height
        self.cellSz = game.grid
        self.position = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)

    def drawApple(self, surface):
        Apple_rect = pygame.Rect(self.position[0], self.position[1], self.cellSz, self.cellSz)
        pygame.draw.rect(surface, (255, 0, 0), Apple_rect)


class Snake(pygame.sprite.Sprite):
    def __init__(self, screen_size, game):
        super().__init__()
        self.screen_size = screen_size
        self.surf = self.image = pygame.Surface((25, 25))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.length = 1
        self.gridW = game.grid_width
        self.gridH = game.grid_height
        self.up = (0, -25)
        self.down = (0, 25)
        self.right = (25, 0)
        self.left = (-25, 0)
        self.direction = random.choice([self.up, self.down, self.left, self.right])
        self.time = 0
        self.time_step = 100
        self.time_now = pygame.time.get_ticks()

    def movement(self, keys):
        if keys[pygame.K_UP]:
            self.direction = self.up
        elif keys[pygame.K_DOWN]:
            self.direction = self.down
        elif keys[pygame.K_RIGHT]:
            self.direction = self.right
        elif keys[pygame.K_LEFT]:
            self.direction = self.left

        if self.time_now - self.time > self.time_step:
            self.rect.move_ip(self.direction)


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()