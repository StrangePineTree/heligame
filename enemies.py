import pygame
from pygame.math import Vector2

class Enemy:
    def __init__(self,pos:Vector2,hp:float, hitbox: pygame.Rect, sprite: pygame.image):
        self.hp = hp
        self.pos = pos
        self.hitbox = hitbox
        self.sprite = sprite

    def update(self):
        pass

class infantry(Enemy):
    def __init__(self, pos):
        super().__init__(pos,10,pygame.Rect(pos.x, pos.y,30,30),pygame.image.load("./graphics/enemies/infantry.png").convert_alpha())

    def update(self):
        #add AI and death here
        #add collision here
        self.pos.x += 1
        self.hitbox = pygame.Rect(self.pos.x, self.pos.y,30,30)
        
