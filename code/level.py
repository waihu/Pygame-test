import pygame
from settings import *
from tile import *
from player import Player
from weapons import *

class Level:
    def __init__(self):
        # Startscreen
        self.gamestate = GameState.NONE
        self.current_map = 0
        self.chestisopen1 = 0
        self.chestisopen2 = 0
        self.swordon = 0
        

    def draw_map(self, map, pos, chest):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # Setup map
        self.create_map(map, chest)

        # Setup player
        self.objects = []
        self.player = Player(pos, [self.visible_sprites], self.obstacle_sprites)
        self.objects.append(self.player)

        for object in self.objects:
            object.render(self.display_surface)


    def create_map(self, i, chest):
        self.i = i
        if (self.i == 0):
            if (self.chestisopen1 == 1):
                chest = 1
            for row_index, row in enumerate(WORLD_MAP0):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if col == " ":
                        Grass((x, y), [self.visible_sprites])
                    if col == "x":
                        Ocean((x, y), [self.visible_sprites, self.obstacle_sprites])
                    if col == "c":
                        self.chestx = x
                        self.chesty = y
                        self.chest = Chest((x, y), [self.visible_sprites], chest)

        if (self.i == 1):
            if (self.chestisopen2 == 1):
                chest = 1
            for row_index, row in enumerate(WORLD_MAP1):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if col == " ":
                        Grass((x, y), [self.visible_sprites])
                    if col == "x":
                        Ocean((x, y), [self.visible_sprites, self.obstacle_sprites])
                    if col == "c":
                        self.chest = Chest((x, y), [self.visible_sprites], chest)
                        

    def reset_map(self):
        self.visible_sprites.empty()
        self.obstacle_sprites.empty()


    def change_map(self):
        posx = 99999
        posy = 99999
        backx = 99999
        backy = 99999
        self.player.swordon = self.swordon

        if (self.current_map == 0):
            posx = 1280
            posy = 640

        if (self.current_map == 1):
            backx = -70
            backy = 128

        if (self.player.rect.x >= posx and self.player.rect.y == posy):
            self.reset_map()
            self.current_map += 1
            self.draw_map(self.current_map, [-20, 160], 0)

        if (self.player.rect.x <= backx and self.player.rect.y == backy):
            self.reset_map()
            self.current_map = self.current_map - 1
            self.draw_map(self.current_map, [1300, 672], 0)


    def openchest(self, pos):
        if (self.current_map == 0):
            if (self.chestisopen1 == 0 and pos[0] > (self.chest.rect.x - 64) and pos[0] < (self.chest.rect.x + 1) and pos[1] > (self.chest.rect.y - 1) and pos[1] < (self.chest.rect.y + 64)):
                self.chestisopen1 = 1
                self.reset_map()
                pos = [pos[0] + 32, pos[1] + 32]
                self.draw_map(self.current_map, pos, 1)
                self.swordon = 1
                self.player.swordon = self.swordon
                print("Swordon is set to 1")

        if (self.current_map == 1):
            if (self.chestisopen2 == 0 and pos[0] > (self.chest.rect.x - 64) and pos[0] < (self.chest.rect.x + 1) and pos[1] > (self.chest.rect.y - 1) and pos[1] < (self.chest.rect.y + 64)):
                self.chestisopen2 = 1
                self.reset_map()
                pos = [pos[0] + 32, pos[1] + 32]
                self.draw_map(self.current_map, pos, 1)


    def showsword(self, pos, screen):
        if (self.player.swordon == 1):
            print("Swordon is set to 2")
            self.sword = Sword([pos[0], pos[1]], [self.visible_sprites])
            self.sword.time = pygame.time.get_ticks()
            self.swordon = 2
            self.player.swordon = self.swordon


    def run(self):
        # Update and draw the game
        self.openchest([self.player.rect.x, self.player.rect.y])
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.change_map()
        
        self.showsword([self.player.rect.x, self.player.rect.y], self.display_surface)        

        ### DEBUGGING
        #print(self.current_map)
        print("x: " + str(self.player.rect.x) + " y: " + str(self.player.rect.y))
        #print(self.player.key_direction)
        self.player.facing()
        


            
