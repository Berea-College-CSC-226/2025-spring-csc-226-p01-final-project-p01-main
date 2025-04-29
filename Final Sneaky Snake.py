import pygame
import tkinter as tk
import tkinter.font as tkfont
import random
import time

class Game:
    def __init__(self):
        self.size = 800, 600
        self.width = 600
        self.height = 800
        self.grid = 25
        self.grid_width = self.width // self.grid
        self.grid_height = self.height // self.grid
        self.score = 0
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.get_buffer()
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.size)

        self.apple = Apple(self)


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.snake.movement(pygame.key.get_pressed())
            self.screen.fill('#FFFFFF')
            self.apple.drawApple(self.screen)
            self.screen.blit(self.snake.surf, self.snake.rect)
            pygame.display.update()
            self.clock.tick(10)



        pygame.quit()

class Apple:
    def __init__(self,game):

        self.gridW = game.grid_width
        self.gridH = game.grid_height
        self.cellSz = game.grid

        self.position = self.random_location()

    def random_location(self):
        x = random.randint(0, self.gridW - 1) * self.cellSz
        y = random.randint(0, self.gridH - 1) * self.cellSz
        return (x, y)


    def randomized_return(self, Snake):
        while True:
            new_position = self.random_location()
            if pygame.sprite.spritecollide(self.Snake, [self.Apple], False):

                else:
                    self.position = new_position

    def drawApple(self, surface):

        Apple_rect = pygame.Rect(self.position[0], self.position[1], self.cellSz, self.cellSz)
        pygame.draw.rect(surface, (255, 0, 0), Apple_rect)




class Snake(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.surf = self.image = pygame.Surface((25, 25))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.x = self.rect.x
        self.length = 1
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





















