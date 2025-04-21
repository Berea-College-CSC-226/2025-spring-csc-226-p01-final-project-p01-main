import pygame
import sys

# Setup
pygame.init()
WIDTH, HEIGHT = 1000, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Lands on Planets")

# Load Images
background = pygame.image.load("planets.gif").convert_alpha()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rocket_img = pygame.image.load("rocket.png").convert_alpha()
rocket_img = pygame.transform.scale(rocket_img, (60, 60))
rocket_img.set_colorkey((255, 255, 255))

# Planet class
class Planet:
    def __init__(self, name, description, x_start, x_end):
        self.name = name
        self.description = description
        self.x_start = x_start
        self.x_end = x_end
        self.hit = False  # Controls if popup was already shown

    def is_hit(self, x):
        return self.x_start <= x <= self.x_end

    def get_info(self):
        return f"{self.name}: {self.description}"

planet_zones = [
    Planet("Venus", "Second planet from the Sun.", 200, 260),
    Planet("Mercury", "Closest to the Sun.", 270, 305),
    Planet("Earth", "Our home planet.", 310, 380),
    Planet("Mars", "The Red Planet.", 400, 460),
    Planet("Jupiter", "The largest planet.", 470, 560),
    Planet("Saturn", "Famous for its rings.", 580, 670),
    Planet("Uranus", "Has a tilted rotation.", 680, 770),
    Planet("Neptune", "Furthest from the Sun.", 790, 860),
]

# Rocket
class Rocket:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = 0
        self.y = HEIGHT // 2 - 30
        self.speed = 20  # Smaller step = better planet detection accuracy
        self.current_planet = None

    def move_right(self):
        self.x += self.speed
        print(f"Rocket X: {self.x}")

    def draw(self):
        screen.blit(rocket_img, (self.x, self.y))

    def check_planet(self):
        for planet in planet_zones:
            if planet.is_hit(self.x) and not planet.hit:
                planet.hit = True
                self.current_planet = planet
                return planet
        return None


# Setup game
rocket = Rocket()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #Moves the rocket to the right by using the key "right"
                rocket.move_right()
            elif event.key == pygame.K_r: #Key "R" sets the rocket to the start
                rocket.reset()
                for p in planet_zones:
                    p.hit = False

    found_planet = rocket.check_planet()
    rocket.draw()

    if rocket.current_planet:
        pygame.draw.rect(screen, (0, 0, 0), (20, 20, 500, 40))
        info_text = font.render(rocket.current_planet.get_info(), True, (255, 255, 255))
        screen.blit(info_text, (30, 30))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()