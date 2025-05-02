import pygame
import tkinter as tk
import tkinter.font as tkfont
import random
import time


class Game:
    def __init__(self):
        self.size = 500, 400
        self.width = 500
        self.height = 400
        self.bottom = 400
        self.top = -25
        self.left = -25
        self.right = 500
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
        self.gridW = self.grid_width
        self.gridH = self.grid_height
        self.cellSz = self.grid
        self.health = 5

        self.food = Food(self)

    def run(self):
        while self.running:
            if (self.snake.rect.x, self.snake.rect.y) == self.food.position:
                self.score += 1
                self.food.position = (
                random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
            if (self.snake.rect.x, self.snake.rect.y) == self.food.position3:
                self.score += 1
                self.food.position3 = (
                random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
            if (self.snake.rect.x, self.snake.rect.y) == self.food.position4:
                self.score += 1
                self.food.position4 = (
                random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
            if (self.snake.rect.x, self.snake.rect.y) == self.food.position5:
                self.score += 1
                self.food.position5 = (
                random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)

            if (self.snake.rect.x, self.snake.rect.y) == self.food.position2:
                self.health -= 1
                self.food.position2 = (
                random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
            if (self.snake.rect.x, self.snake.rect.y) == self.food.position6:
                self.health -= 1
                self.food.position6 = (
                random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
            if (self.snake.rect.x, self.snake.rect.y) == self.food.position7:
                self.health -= 1
                self.food.position7 = (
                random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
            if (self.snake.rect.x, self.snake.rect.y) == self.food.position8:
                self.health -= 1
                self.food.position8 = (
                random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)

            if self.snake.rect.x == self.left:
                self.running = False
            if self.snake.rect.y == self.bottom:
                self.running = False
            if self.snake.rect.x == self.right:
                self.running = False
            if self.snake.rect.y == self.top:
                self.running = False
            if self.health <= 0:
                self.running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.snake.movement(pygame.key.get_pressed())
            self.screen.fill('#FFFFFF')
            self.food.drawBomb(self.screen)
            self.food.drawApple(self.screen)
            self.screen.blit(self.snake.surf, self.snake.rect, )
            pygame.display.set_caption("MINEFIELD:  " + "Score:" + str(self.score) + "  Health: " + str(self.health))
            pygame.display.update()
            self.clock.tick(10)

        pygame.quit()


class Food:
    def __init__(self, game):
        self.gridW = game.grid_width
        self.gridH = game.grid_height
        self.cellSz = game.grid
        self.position = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
        self.position2 = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
        self.position3 = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
        self.position4 = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
        self.position5 = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
        self.position6 = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
        self.position7 = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)
        self.position8 = (
        random.randint(0, self.gridW - 1) * self.cellSz, random.randint(0, self.gridH - 1) * self.cellSz)

    def drawApple(self, surface):
        pygame.draw.rect(surface, (0, 255, 0),
                         pygame.Rect(self.position[0], self.position[1], self.cellSz, self.cellSz))
        pygame.draw.rect(surface, (0, 255, 0),
                         pygame.Rect(self.position3[0], self.position3[1], self.cellSz, self.cellSz))
        pygame.draw.rect(surface, (0, 255, 0),
                         pygame.Rect(self.position4[0], self.position4[1], self.cellSz, self.cellSz))
        pygame.draw.rect(surface, (0, 255, 0),
                         pygame.Rect(self.position5[0], self.position5[1], self.cellSz, self.cellSz))

    def drawBomb(self, surface):
        pygame.draw.rect(surface, (255, 0, 0),
                         pygame.Rect(self.position2[0], self.position2[1], self.cellSz, self.cellSz))
        pygame.draw.rect(surface, (255, 0, 0),
                         pygame.Rect(self.position6[0], self.position6[1], self.cellSz, self.cellSz))
        pygame.draw.rect(surface, (255, 0, 0),
                         pygame.Rect(self.position7[0], self.position7[1], self.cellSz, self.cellSz))
        pygame.draw.rect(surface, (255, 0, 0),
                         pygame.Rect(self.position8[0], self.position8[1], self.cellSz, self.cellSz))


class Snake(pygame.sprite.Sprite):
    def __init__(self, screen_size, game):
        super().__init__()
        self.screen_size = screen_size
        self.surf = self.image = pygame.Surface((25, 25))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = pygame.draw.rect(self.surf, (0, 0, 0), pygame.Rect(0, 0, 25, 25))
        self.rect.move_ip(self.screen_size[0] // 2, self.screen_size[1] // 2)
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