import pygame
import sys
from dataclasses import dataclass
# Planet class
# dataclass was explained by TA (Nauka) for unit test file in order to test "check_planet" method
@dataclass

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


# Rocket
class Rocket:
    def __init__(self):
        self.reset()

    def reset(self, HEIGHT=300):
        self.x = 0
        self.y = HEIGHT // 2 - 70
        self.speed = 20  # Smaller step = better planet detection accuracy
        self.current_planet = None

    def move_right(self):
        self.x += self.speed
        print(f"Rocket X: {self.x}")

    def draw(self):
        screen.blit(rocket_img, (self.x, self.y))

    def check_planet(self, planetS, testing=False):
        for planet in planetS:
            if testing:
                self.current_planet = planet
                return planet

            if planet.is_hit(self.x) and not planet.hit:
                planet.hit = True
                self.current_planet = planet
                return planet
        return None

def show_planet_screen(self):
    showing = True
    font = pygame.font.SysFont(None, 40)
    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    showing = False
        screen.fill((0,0,50))
        name_text = font.render(f"Welcome to {planet.name}!", True, (255,255,255))
        desc_text = font.render(planet.description, True, (150,150,150))
        tip_text = font.render("Press ESC to return", True, (150,150,150))

        screen.blit(name_text, (WIDTH // 4, HEIGHT // 3))
        screen.blit(desc_text, (WIDTH // 4, HEIGHT // 3 + 40))
        screen.blit(tip_text, (WIDTH // 4, HEIGHT // 3 + 80))

        pygame.display.update()



if __name__ == "__main__":
    # Setup
    pygame.init()
    WIDTH, HEIGHT = 1000, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rocket Lands on Planets")

    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)
    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('land', True, color)

    # Load Images
    WIDTH, HEIGHT = 1000, 189
    background = pygame.image.load("planets.gif").convert_alpha()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    WIDTH, HEIGHT = 1000, 300
    rocket_img = pygame.image.load("rocket.png").convert_alpha()
    rocket_img = pygame.transform.scale(rocket_img, (45, 45))
    rocket_img.set_colorkey((255, 255, 255))

    planet_zones = [
        Planet("Venus", "Second planet from the Sun.", 200, 230),
        Planet("Mercury", "Closest to the Sun.", 255, 295),
        Planet("Earth", "Our home planet.", 340, 380),
        Planet("Mars", "The Red Planet.", 420, 450),
        Planet("Jupiter", "The largest planet.", 470, 560),
        Planet("Saturn", "Famous for its rings.", 600, 670),
        Planet("Uranus", "Has a tilted rotation.", 700, 770),
        Planet("Neptune", "Furthest from the Sun.", 790, 860),
    ]
    # Rocket


    # Setup game
    rocket = Rocket()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 30)

    running = True
    while running:
        screen.fill((0,0,0))
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if rocket.current_planet and width / 2.5 <= mouse[0] <= width / 2.5 + 140 and height / 1.58 <= mouse[1] <= height / 1.58 + 40:
                    show_planet_screen(rocket.current_planet)


        rocket.current_planet = None
        for planet in planet_zones:
            if planet.is_hit(rocket.x):
                rocket.current_planet = planet
                break
        rocket.draw()

        if rocket.current_planet:

            pygame.draw.rect(screen, color_light, [width / 2.5, height / 1.58, 140, 40])
            screen.blit(text, (width / 2.5 + 40, height / 1.58))
        else:
            pygame.draw.rect(screen, (0, 0, 0), [width / 2.5, height / 1.58, 140, 40])

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()


'''important note *** when we integrate a button we should have the event handler for text, we just have a button pop up
when a planet is hit then we handle screen and changing them'''