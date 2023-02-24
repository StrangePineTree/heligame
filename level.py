import pygame
import random
from generation import *
from settings import *
from sprites import GenericSprite
from player import Player
from player import *
from generation import enemyList
from enemies import *
from weapons import *
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()

        self.setup()

        self.groundPos = self.player.pos.x-200

#TODO: completly redo collisoon, its fucked and cant be fixxed
    def setup(self):
        for x in range (0,1):
            enemyList.append(infantry(Vector2(0,SCREEN_HEIGHT-118)))
        for x in range (0,1):
            enemyList.append(tank(Vector2(250,SCREEN_HEIGHT-148)))
        for x in range (0,1):
            enemyList.append(maus(Vector2(600,SCREEN_HEIGHT-178)))

        self.player = Player((640, SCREEN_HEIGHT-130), self.all_sprites)

        GenericSprite(
            pos = (SCREEN_WIDTH/2,SCREEN_HEIGHT+100),
            surf = pygame.image.load("./graphics/background/background (sky).png").convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['sky'],
            point = ('midbottom')
        )
        GenericSprite(
            pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT+100),
            surf = pygame.image.load("./graphics/background/ground.png").convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground'],
            point = ('topleft')
        )

        for x in range (0,1000):
            GenerateObstacle(self)

    def run(self,dt):
        self.display_surface.fill((74, 65, 42))
        self.all_sprites.update(dt)
        self.all_sprites.custom_draw(self.player)
        if OVERLAY == True:
            self.player.displayGUI()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()


    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    if layer == 2:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset / PARALLAX_FACTOR * (.1 if layer == 1 else .8)
                        self.display_surface.blit(sprite.image, offset_rect)
                    elif layer == 3:
                        tiles = math.ceil(SCREEN_WIDTH / sprite.image.get_width()) + 2
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        for i in range(tiles):
                            #sprite.image.get_rect(center=(0,SCREEN_HEIGHT-100))
                            drawRect = sprite.rect.copy()
                            drawRect.center = (sprite.image.get_width()*(i - 1) + player.scroll.x, SCREEN_HEIGHT-11-self.offset.y)
                            self.display_surface.blit(sprite.image, (sprite.image.get_width()*(i - 1) + player.scroll.x, SCREEN_HEIGHT-100-self.offset.y))  
                            i += 1
                        if abs(player.scroll.x) > (sprite.image.get_width()):
                            player.scroll.x = 0

                        #pygame.draw.rect(self.display_surface, (100,200,100),[250-self.offset.x,SCREEN_HEIGHT-250-self.offset.y,50,25])

                    elif layer == 1:
                        tiles = math.ceil(SCREEN_WIDTH / sprite.image.get_width()) + 2
                        offset_rect = sprite.rect.copy()
                        offset_rect.midbottom -= self.offset / PARALLAX_FACTOR * .1
                        for i in range(tiles):
                            #sprite.image.get_rect(center=(0,SCREEN_HEIGHT-100))
                            drawRect = sprite.rect.copy()
                            drawRect.midbottom = (sprite.image.get_width()*(i - 1) + player.scrollParralax.x, SCREEN_HEIGHT-100-self.offset.y/PARALLAX_FACTOR*.2)
                            self.display_surface.blit(sprite.image, (sprite.image.get_width()*(i - 1) + player.scrollParralax.x, SCREEN_HEIGHT-1800-self.offset.y/PARALLAX_FACTOR*.2))  
                            i += 1
                        if abs(player.scrollParralax.x) > (sprite.image.get_width()):
                            player.scrollParralax.x = 0

                    elif layer == 6:
                        for e in enemyList:
                            e.draw(self.offset)
                        offset_rect = sprite.rect.copy()
                        offset_rect.midbottom -= self.offset
                        self.display_surface.blit(sprite.image, offset_rect)
                        for a in attacklist:
                            if a.rotated == False:
                                self.image = pygame.transform.rotate(a.sprite, a.angle-180)
                                self.rect = self.image.get_rect()
                                self.rect.center = a.pos 
                                a.rotated = True
                            self.display_surface.blit(self.image, a.pos-self.offset)