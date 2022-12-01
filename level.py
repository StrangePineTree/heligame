import pygame
from settings import *
from sprites import Generic
from player import Player
from player import *
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
        Generic(
            pos = (0,400),
            surf = pygame.image.load("./graphics/background/background (forrest).png").convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['background']
        )
        Generic(
            pos = (0,SCREEN_HEIGHT-100),
            surf = pygame.image.load("./graphics/background/ground.png").convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['ground']
        )

        self.player = Player((640, 360), self.all_sprites)

    def run(self,dt):
        self.display_surface.fill((97,62,86))
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
                    if layer <= 2:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset / PARALLAX_FACTOR * (.1 if layer == 1 else .8)
                        self.display_surface.blit(sprite.image, offset_rect)
                    elif layer == 3:
                        self.tiles = math.ceil(SCREEN_WIDTH / sprite.image.get_width()) + 1
                        self.i = 0
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        while(self.i < self.tiles):
                            $sprite.image.get_rect(center=(0,SCREEN_HEIGHT-100))
                            self.display_surface.blit(sprite.image, (sprite.image.get_width()*self.i + player.scroll.x, SCREEN_HEIGHT-100-self.offset.y))  
                            self.i += 1
                        if abs(player.scroll.x) > (sprite.image.get_width()):
                            player.scroll.x = 0
                        print(player.scroll.x)
                    else:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        self.display_surface.blit(sprite.image, offset_rect)
