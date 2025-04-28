import pygame
import sys
from dataclasses import dataclass
# Planet class
# dataclass was explained by TA (Nauka) for unit test file in order to test "check_planet" method
@dataclass

class Planet:
    def __init__(self, name, description, x_start, x_end, image):
        self.name = name
        self.description = description
        self.x_start = x_start
        self.x_end = x_end
        self.image = image
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
        self.y = HEIGHT // 2 + 150
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

def show_planet_screen(planet):
    showing = True
    font = pygame.font.SysFont(None, 40)

    planet_image = pygame.image.load(planet.image).convert_alpha()
    planet_image = pygame.transform.scale(planet_image, (300, 300))

    while showing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    showing = False
        screen.fill((0,0,0))
        name_text = font.render(f"Welcome to {planet.name}!", True, (255,255,255))
        desc_text = font.render(planet.description, True, (150,150,150))
        tip_text = font.render("Press ESC to return", True, (150,150,150))

        screen.blit(name_text, (WIDTH // 4, HEIGHT // 3 + 150))
        screen.blit(desc_text, (WIDTH // 4, HEIGHT // 3 + 190))
        screen.blit(tip_text, (WIDTH // 4, HEIGHT // 3 + 230))
        screen.blit(planet_image, (WIDTH // 2 - 150, HEIGHT // 2 - 310 ))

        pygame.display.update()



if __name__ == "__main__":
    # Setup
    pygame.init()
    WIDTH, HEIGHT = 1280, 655
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Rocket Lands on Planets")

    color = (255, 255, 255)
    color_light = (170, 170, 170)
    color_dark = (100, 100, 100)

    width = screen.get_width()
    height = screen.get_height()
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('LAND', True, color)

    # Load Images
    background = pygame.image.load("planets.gif").convert_alpha()
    background = pygame.transform.scale(background, (1280, 250))
    back_rect = background.get_rect()
    back_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
    screen.blit(background, back_rect)






    rocket_img = pygame.image.load("rocket.png").convert_alpha()
    rocket_img = pygame.transform.scale(rocket_img, (50, 50))
    rocket_img.set_colorkey((255, 255, 255))

    planet_zones = [
        Planet("Venus", "Second planet from the Sun.", 240, 280, "venus-mariner-10-pia23791-fig2.jpg"),
        Planet("Mercury", "Closest to the Sun.", 340, 380, "Mercury_in_true_color.jpg"),
        Planet("Earth", "Our home planet.", 440, 480, "The_Earth_seen_from_Apollo_17.jpg"),
        Planet("Mars", "The Red Planet.", 540, 560, "Mars_-_August_30_2021_-_Flickr_-_Kevin_M._Gill.png"),
        Planet("Jupiter", "The largest planet.", 620, 700, "Jupiter.jpg"),
        Planet("Saturn", "Famous for its rings.", 760, 840, "istockphoto-1496413363-612x612.jpg"),
        Planet("Uranus", "Has a tilted rotation.", 900, 960, "Uranus_Voyager2_color_calibrated.png"),
        Planet("Neptune", "Furthest from the Sun.", 1020, 1100, "Neptune_-_Voyager_2_(29347980845)_flatten_crop.jpg"),
    ]
    # Rocket


    # Setup game
    rocket = Rocket()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)

    running = True
    while running:
        screen.fill((0,0,0))
        screen.blit(background, back_rect)

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
                if rocket.current_planet and width / 2.37 <= mouse[0] <= width / 2.37 + 140 and height / 1.445 <= mouse[1] <= height / 1.445 + 40:
                    show_planet_screen(rocket.current_planet)


        rocket.current_planet = None
        for planet in planet_zones:
            if planet.is_hit(rocket.x):
                rocket.current_planet = planet
                break
        rocket.draw()

        if rocket.current_planet:

            pygame.draw.rect(screen, color_light, [width / 2.37, height / 1.445, 180, 60])
            screen.blit(text, (width / 2.37 + 50, height / 1.445 + 10))
        else:
            pygame.draw.rect(screen, (0, 0, 0), [width / 2.37, height / 1.445, 180, 60])

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()


'''important note *** when we integrate a button we should have the event handler for text, we just have a button pop up
when a planet is hit then we handle screen and changing them'''