import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assests()
        self.status = 'right'
        self.frame_index = 0

        self.image = self.animations[self.status]

        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 300

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
        
    def move(self,dt):
        if self.direction.magnitude() >0:
            self.direction = self.direction.normalize()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def import_assests(self):
        self.animations = {'left':[], 'right':[]}#when moving will rotate image by x degrees
        for animation in self.animations.keys():
            full_path = './graphics/heli/' + animation
            self.animations[animation]=import_folder(full_path)
        

    def update(self, dt):
        self.input()
        self.move(dt)