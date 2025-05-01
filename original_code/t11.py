import pygame
from t11_NPC import GoodNPC, EvilNPC
from t11_player import Player


class Game:
    def __init__(self):
        """
        Game class for handling the game logic.
        """
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill('#9CBEBA')
        self.clock = pygame.time.Clock()
        self.tuna = Player(self.size)
        self.tacocat = GoodNPC(self.size)
        self.whiskers = EvilNPC(self.size)

        self.npc_group = pygame.sprite.Group(self.tacocat, self.whiskers)


    def run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:
            # Handle game ending first
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            # Handle user and game events next
            if pygame.sprite.spritecollide(self.tuna, self.npc_group, False):
                font = pygame.font.SysFont("ComicSans", 36)

                if pygame.sprite.spritecollide(self.tuna, [self.tacocat], False):
                # Collision! Prints the game ending text to the screen.
                    txt = font.render('Taco, you caught me!!', True, "darkblue")

                elif pygame.sprite.spritecollide(self.tuna, [self.whiskers], False):
                # Collision! Prints the game ending text to the screen.
                    txt = font.render('Whiskers, you caught me!!', True, "darkblue")
                self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            else:
                # Keep playing!
                self.tuna.movement(pygame.key.get_pressed())
                self.tacocat.movement()
                self.whiskers.movement()
                self.screen.fill('#9CBEBA')
                self.screen.blit(self.tuna.surf, self.tuna.rect)
                self.screen.blit(self.tacocat.surf, self.tacocat.rect)
                self.screen.blit(self.whiskers.surf, self.whiskers.rect)
            pygame.display.update()
            self.clock.tick(24)

        pygame.quit()


def main():
    """
    Starts the cat game.

    :return: None
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
