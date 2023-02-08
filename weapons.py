import pygame
from pygame.math import Vector2
import math


class Weapon:
    def __init__(self,sourcePos: Vector2,speed:float, playerMissile: float,target:Vector2, sprite: pygame.surface.Surface):
        self.pos = sourcePos.copy()
        self.sourcePos = sourcePos
        self.sprite = sprite
        self.speed = speed
        self.playerMissile = playerMissile
        self.target = target
        self.delete = False
        self.rotated = False
        self.hitbox = 0
        self.lifetime = 0
        self.damage = 0

    def update(self):
        pass

class Missile(Weapon):
    def __init__(self, sourcePos, speed,playerMissile,target):
        super().__init__(sourcePos,speed,playerMissile,target,pygame.image.load("./graphics/weapons/missile.png").convert_alpha())
        self.vel = (self.target - self.sourcePos).normalize()
        self.angle = (self.target - self.sourcePos).angle_to((1, 0))
        self.hitbox =  pygame.image.load("./graphics/weapons/missile.png").get_rect()
        self.damage = 50

    def update(self):
        self.pos += self.vel * self.speed 
        self.lifetime += 1
    def kill(self):
        self.delete = True
        #add explosion here

attacklist: list[Weapon] = []
