import pygame
from pygame.math import Vector2

class Weapon:
    def __init__(self,pos: Vector2,speed:float, playerMissile: float,target:Vector2, sprite: pygame.image):
        self.pos = pos
        self.sprite = sprite
        self.speed = speed
        self.playerMissile = playerMissile
        self.target = target

    def update(self):
        pass

class Missile(Weapon):
    def __init__(self, pos):
        super().__init__(pos,10,self.playerMissile,pygame.image.load("./graphics/weapons/missile.png").convert_alpha())

    def update(self):
        self.pos.x += 1

atttacklist: list[Weapon] = []
