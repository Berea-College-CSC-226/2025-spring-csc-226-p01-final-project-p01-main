import pygame
import sys
from game_logic import Planet, Rocket

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

# Setup game
rocket = Rocket()
clock = pygame.time.Clock()

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.move_right()
            elif event.key == pygame.K_r:
                rocket.reset()
                for p in planet_zones:
                    p.hit = False

    found_planet = rocket.check_planet(planet_zones)
    rocket.draw(screen, rocket_img)

    if rocket.current_planet:
        pygame.draw.rect(screen, (0, 0, 0), (20, 20, 500, 40))
        info_text = pygame.font.SysFont(None, 30).render(rocket.current_planet.get_info(), True, (255, 255, 255))
        screen.blit(info_text, (30, 30))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()
