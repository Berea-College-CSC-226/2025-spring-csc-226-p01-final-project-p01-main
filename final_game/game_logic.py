import pygame

# Planet class
class Planet:
    def __init__(self, name, description, x_start, x_end):
        self.name = name
        self.description = description
        self.x_start = x_start
        self.x_end = x_end
        self.hit = False

    def is_hit(self, x):
        return self.x_start <= x <= self.x_end

    def get_info(self):
        return f"{self.name}: {self.description}"

# Rocket class
class Rocket:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = 0
        self.y = 150
        self.speed = 20
        self.current_planet = None

    def move_right(self):
        self.x += self.speed

    def draw(self, screen, rocket_img):
        screen.blit(rocket_img, (self.x, self.y))

    def check_planet(self, planet_zones):
        for planet in planet_zones:
            if planet.is_hit(self.x) and not planet.hit:
                planet.hit = True
                self.current_planet = planet
                return planet
        return None
