import pygame
from settings import *
from sprites import Generic
from player import Player
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()

        self.setup()
        

    def setup(self):
        Generic(
            pos = (0,0),
            surf = pygame.image.load("./graphics/background/background (sky).jpg").convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['sky']
        )
        self.player = Player((640, 360), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill((0,143,200))
        self.all_sprites.update(dt)
        self.all_sprites.custom_draw(self.player)


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
                    if layer <= 3:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset.y
                        self.display_surface.blit(sprite.image, offset_rect)                        
                    else:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        self.display_surface.blit(sprite.image, offset_rect)
