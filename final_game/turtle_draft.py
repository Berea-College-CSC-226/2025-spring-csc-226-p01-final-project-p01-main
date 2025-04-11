

import pygame
import random


# Planet class to represent each planet
class Planet:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def Planets(self):
        self.planets = [
            Planet("Mercury", "Mercury is the closest planet to the Sun.", ),
            Planet("Venus", "Venus is the second planet from the Sun."),
            Planet("Earth", "Earth is our home planet, the third from the Sun."),
            Planet("Mars", "Mars is the fourth planet from the Sun, known as the Red Planet."),
            Planet("Jupiter", "Jupiter is the fifth planet and the largest in our solar system."),
            Planet("Saturn", "Saturn is famous for its beautiful rings."),
            Planet("Uranus", "Uranus is the seventh planet, known for its tilted axis."),
            Planet("Neptune", "Neptune is the eighth and farthest planet from the Sun."),
        ]

    def get_info(self):
        return f"{self.name}: {self.description}"

# Rocket class to represent the rocket's movement
class Rocket(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        self.position = None  # The planet the rocket lands on
        self.surf = pygame.image.load("vector-illustration-rocket-icon-image-png-701751694966760xqxrwxd6te.png").convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()


    def move(self, planets):
        # Simulating rocket movement for 2 seconds
        self.position = random.choice(Planet.Planets())
        print(f"The rocket has landed on {self.position.name}!")

# Game class to manage the overall game logic
class Game:
    def __init__(self):
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill("blue")
        self.clock = pygame.time.Clock()
        self.rocket = Rocket(self.size)
    def run(self):
        while self.running:
            self.screen.blit(self.rocket.surf, self.rocket.rect)
        pygame.display.update()
        self.clock.tick(24)



    def start_game(self):
        # Start the rocket movement
        self.rocket.move(Planet.Planets)

        # Display planet information
        planet_info = self.rocket.position.get_info()
        print(planet_info)


if __name__ == "__main__":
    game = Game()
    game.start_game()




