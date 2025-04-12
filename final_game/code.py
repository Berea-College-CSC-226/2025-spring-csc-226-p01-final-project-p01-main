

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen Setup
WIDTH, HEIGHT = 1000, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Lands on Planets")

# Load your images
background = pygame.image.load("planets.gif").convert_alpha()  # use your actual background PNG
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rocket_img = pygame.image.load("vector-illustration-rocket-icon-image-png-701751694966760xqxrwxd6te.png").convert_alpha()
rocket_img = pygame.transform.scale(rocket_img, (60, 60))
rocket_img.set_colorkey((255, 255, 255))

# Planet zones based on their X-position in the background
class Planet:
    def __init__(self, name, description, x_start, x_end):
        self.name = name
        self.description = description
        self.x_start = x_start
        self.x_end = x_end

    def is_hit(self, x):
        return self.x_start <= x <= self.x_end

    def get_info(self):
        return f"{self.name}: {self.description}"

planet_zones = [
    Planet("Mercury", "Closest to the Sun.", 50, 120),
    Planet("Venus", "Second planet.", 130, 200),
    Planet("Earth", "Our home planet.", 210, 280),
    Planet("Mars", "Red Planet.", 290, 360),
    Planet("Jupiter", "Biggest planet.", 370, 440),
    Planet("Saturn", "Has rings.", 450, 520),
    Planet("Uranus", "Tilted axis.", 530, 600),
    Planet("Neptune", "Farthest away.", 610, 680),
]

# Rocket class
class Rocket:
    def __init__(self):
        self.x = 0
        self.y = HEIGHT // 2 - 30
        self.speed = 5
        self.landed = False
        self.planet = None

    def move_right(self):
        if not self.landed:
            self.x += self.speed

    def draw(self):
        screen.blit(rocket_img, (self.x, self.y))

    def check_for_landing(self):
        for planet in planet_zones:
            if planet.is_hit(self.x):
                self.landed = True
                self.planet = planet
                print(f"The rocket has landed on {planet.name}!")
                print(planet.get_info())
                break

# Main loop
clock = pygame.time.Clock()
rocket = Rocket()
font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move rocket automatically to the right
    rocket.move_right()
    rocket.check_for_landing()
    rocket.draw()

    # Show planet info if landed
    if rocket.landed and rocket.planet:
        info_text = font.render(rocket.planet.get_info(), True, (255, 255, 255))
        screen.blit(info_text, (20, 20))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
