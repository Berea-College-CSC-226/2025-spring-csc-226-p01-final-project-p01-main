import pygame
import tkinter
import tkinter as tk
import tkinter.font as tkfont


class Game:
    def __init__(self):
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#FFFFFF')
        self.clock = pygame.time.Clock()
        self.snake = Snake(self.size)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                keys = pygame.key.get_pressed() #new line added
                self.snake.update_direction(keys)
                self.snake.movement() #edited
                self.screen.fill('#FFFFFF')
                self.screen.blit(self.snake.surf, self.snake.rect)
            pygame.display.update()
            self.clock.tick(60) #changed from 25 to 60

        pygame.quit()


class Snake(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.surf = self.image = pygame.Surface((25, 25))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0] // 2, self.screen_size[1] // 2)
        self.direction = pygame.Vector2(0,0) #new line of code added
        self.speed = 5 #new line of code, smaller step size for more smooth movement

    def update_direction(self, keys): #new class name and conditions
        if keys[pygame.K_UP]:
            self.direction = pygame.Vector2(0,-1)
        elif keys[pygame.K_DOWN]:
            self.direction = pygame.Vector2(0,1)
        if keys[pygame.K_RIGHT]:
            self.direction = pygame.Vector2(1,0)
        elif keys[pygame.K_LEFT]:
            self.direction = pygame.Vector2(-1,0)

    def movement(self):
        self.rect.move_ip(self.direction * self.speed)  #changed class to make smooth move

def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()