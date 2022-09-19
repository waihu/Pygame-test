import pygame
from settings import * 

class Grass(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("imgs/grass1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Ocean(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("imgs/ocean1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Chest(pygame.sprite.Sprite):
    def __init__(self, pos, groups, isopen):
        super().__init__(groups)
        if (isopen == 0):
            self.image = pygame.image.load("imgs/chest.png").convert_alpha()
        elif (isopen == 1):
            self.image = pygame.image.load("imgs/chestopen.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)