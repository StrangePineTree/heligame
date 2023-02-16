import pygame
from pygame.math import Vector2
import math
import random
from weapons import *

class Enemy:
    def __init__(self,pos:Vector2,hp:float, hitbox: pygame.Rect, sprite: pygame.surface.Surface):
        self.hp = hp
        self.pos = pos
        self.hitbox = hitbox
        self.sprite = sprite
        self.state = 'patrol'
        self.walkDist = -100
        self.direction = 1
        self.swapped = False
        self.display_surface = pygame.display.get_surface()

    def update(self):
        pass

    def draw(self, offset):
        pass

class infantry(Enemy):
    def __init__(self, pos):
        super().__init__(pos,10,pygame.Rect(pos.x, pos.y,30,30),pygame.image.load("./graphics/enemies/infantry.png").convert_alpha())
        self.startPos = pos

    '''
    eventually there will be 3 states
    patrol: infantry will just walk randomly
    gaurd: infantry will walk randomly but will not go far from a certian point
    agro: when player is close infantry will attack it
    '''
    def update(self,playerPos:Vector2):
        if math.dist(playerPos,self.pos) < 500:
            self.state = 'agro'
        elif math.dist(playerPos,self.pos) < 1500:
            self.state = 'patrol'
        if self.state == 'patrol':
            if self.walkDist <= -10:
                randnum = random.randint(1,2)
                if randnum == 1:
                    self.direction = 1
                else: self.direction = -1
                self.walkDist = random.randint(550,2000)
            if self.walkDist >0:
                self.pos.x += .5 * self.direction
            self.walkDist -=1
        if self.state == 'agro':
            randnum = random.randint(1,50)
            if randnum == 1:
                attacklist.append(Missile(self.pos,(10),False,(playerPos + Vector2(random.randrange(-50,50),random.randrange(-50,50)))))

        self.hitbox = pygame.Rect(self.pos.x, self.pos.y,30,30)

    def draw(self,offset):
        self.display_surface.blit(self.sprite, self.pos-offset)

    

class tank(Enemy):
    def __init__(self, pos):
        super().__init__(pos,10,pygame.Rect(pos.x, pos.y,30,30),pygame.image.load("./graphics/enemies/tank(left).png").convert_alpha())
        self.startPos = pos
        self.left = pygame.image.load("./graphics/enemies/tank(left).png").convert_alpha()
        self.right = pygame.image.load("./graphics/enemies/tank(right).png").convert_alpha()

    def update(self,playerPos:Vector2): 
        if self.state == 'patrol':
            if self.walkDist <= -10:
                self.swapped = False
                randnum = random.randint(1,2)
                if randnum == 1:
                    self.direction = 1
                    if self.swapped == False:
                        self.sprite = self.right
                        self.swapped = True
                else: 
                    self.direction = -1
                    if self.swapped == False:
                        self.sprite = self.left
                        self.swapped = True
                self.walkDist = random.randint(550,2000)
            if self.walkDist >0:
                self.pos.x += .5 * self.direction
            self.walkDist -=1

        self.hitbox = pygame.Rect(self.pos.x, self.pos.y,30,30)#update hitbox here

    def draw(self,offset):
        self.display_surface.blit(self.sprite, self.pos-offset)
        
class maus(Enemy):
    def __init__(self, pos):
        super().__init__(pos,10,pygame.Rect(pos.x, pos.y,30,30),pygame.image.load("./graphics/enemies/boss/maus(left).png").convert_alpha())
        self.startPos = pos
        self.left = pygame.image.load("./graphics/enemies/boss/maus(left).png").convert_alpha()
        self.right = pygame.image.load("./graphics/enemies/boss/maus(right).png").convert_alpha()

    def update(self,playerPos:Vector2): 
        if self.state == 'patrol':
            if self.walkDist <= -10:
                self.swapped = False
                randnum = random.randint(1,2)
                if randnum == 1:
                    self.direction = 1
                    if self.swapped == False:
                        self.sprite = self.right
                        self.swapped = True
                else: 
                    self.direction = -1
                    if self.swapped == False:
                        self.sprite = self.left
                        self.swapped = True
                self.walkDist = random.randint(550,2000)
            if self.walkDist >0:
                self.pos.x += .15 * self.direction
            self.walkDist -=1

        self.hitbox = pygame.Rect(self.pos.x, self.pos.y,30,30)#update hitbox here

    def draw(self,offset):
        self.display_surface.blit(self.sprite, self.pos-offset)