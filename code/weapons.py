import pygame
from settings import *


class Sword(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("imgs/sword/full.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.time = None

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= 750:
                self.kill()
        
        

    
