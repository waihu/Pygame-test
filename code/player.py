import pygame
from settings import *
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        
        self.image = pygame.image.load("imgs/Player/player.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        # Movement:
        self.Facing = ""
        self.key_direction = [0, 0]
        self.speed = 5

        # Obstacles
        self.obstacle_sprites = obstacle_sprites  
        
        # Weapons
        self.swordon = 0


    def input(self):
        keys = pygame.key.get_pressed()
        
        self.leftPressed = pygame.mouse.get_pressed()[0]

        if keys[pygame.K_w]:
            self.key_direction[0] = -1
        elif keys[pygame.K_s]:
            self.key_direction[0] = 1
        else:
            self.key_direction[0] = 0

        if keys[pygame.K_a]:
            self.key_direction[1] = -1
        elif keys[pygame.K_d]:
            self.key_direction[1] = 1
        else:
            self.key_direction[1] = 0


    def move(self, speed):
        if (self.key_direction[0] == -1 and self.key_direction[1] == -1): 
            speed = float(math.sqrt(speed**2/2))
        elif (self.key_direction[0] == 1 and self.key_direction[1] == 1):
            speed = float(math.sqrt(speed**2/2))
        elif (self.key_direction[0] == 1 and self.key_direction[1] == -1):
            speed = float(math.sqrt(speed**2/2))
        elif (self.key_direction[0] == -1 and self.key_direction[1] == 1):
            speed = float(math.sqrt(speed**2/2))

        self.rect.y += self.key_direction[0] * speed
        self.collision("vertical")
        self.rect.x += self.key_direction[1] * speed
        self.collision("horizontal")


    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.key_direction[1] == 1: #Moving right
                        self.rect.right = sprite.rect.left
                    if self.key_direction[1] == -1: #Moving left
                        self.rect.left = sprite.rect.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.key_direction[0] == 1: #Moving down
                        self.rect.bottom = sprite.rect.top
                    if self.key_direction[0] == -1: #Moving up
                        self.rect.top = sprite.rect.bottom


    def facing(self):
        if (self.key_direction[0] == 0 and self.key_direction[1] == 1):
            self.Facing = "right"
        if (self.key_direction[0] == 0 and self.key_direction[1] == -1):
            self.Facing = "left"
        if (self.key_direction[0] == 1 and self.key_direction[1] == 0):
            self.Facing = "Down"
        if (self.key_direction[0] == -1 and self.key_direction[1] == 0):
            self.Facing = "Up"
#       if (self.key_direction[0] == -1 and self.key_direction[1] == 1):
#           self.Facing = "Upright"
#       if (self.key_direction[0] == -1 and self.key_direction[1] == -1):
#           self.Facing = "Upleft"
#       if (self.key_direction[0] == 1 and self.key_direction[1] == 1):
#           self.Facing = "Downright"
#       if (self.key_direction[0] == 1 and self.key_direction[1] == -1):
#           self.Facing = "Downleft"
        
        print(self.Facing)


    def attack(self):
        if self.swordon == 2:
            if self.leftPressed:
                print("Attacking!")
                

    def render(self, screen):
        screen.blit(self.image, self.rect)


    def update(self):
        self.input()
        self.move(self.speed)
        self.attack()
        
        



    
