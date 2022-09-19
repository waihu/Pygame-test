import pygame, sys
from settings import *
from level import Level
from time import sleep

class Game:
    def __init__(self):
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Set game caption:
        pygame.display.set_caption("Game")
        self.clock = pygame.time.Clock()

        #self.level = Level(0)

    def run(self):
        self.mapnum = 0
        self.level = Level()
        self.setup = 0
        while True:
            # Startscreen
            while self.level.gamestate == GameState.NONE:
                self.screen.fill((144,238,144))
                self.clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.level.gamestate = GameState.RUNNING
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                pygame.display.flip()

            ### Game
            # Setup map
            while self.level.gamestate == GameState.RUNNING:
                while self.setup == 0:
                    print("Setting up")
                    self.level.draw_map(self.mapnum, [155,155], 0)
                    self.setup = 1

                while self.setup == 1 and self.level.gamestate == GameState.RUNNING:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                self.level.gamestate = GameState.NONE
                                
                                                      

                    self.screen.fill("black")
                    self.level.run()
                    pygame.display.update()
                    self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
