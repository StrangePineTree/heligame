import pygame
from settings import *

class GenericSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['enemies'], point=''):
        
        super().__init__(groups)
        self.image = surf
        self.rect = (self.image.get_rect(topleft = pos) if point == 'topleft' else (self.image.get_rect(midbottom = pos)))
        self.z = z
