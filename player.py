import pygame
from settings import *
from support import *
from pygame.math import Vector2

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

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed: Vector2 = Vector2(0, 0)
        self.rotation = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.speed.y += -THRUST
        elif keys[pygame.K_s]:
            self.speed.y += THRUST
        if keys[pygame.K_a]:
            self.speed.x += -THRUST
            self.status = 'left'
            if self.rotation <= 20:
                self.rotation += .1
        elif keys[pygame.K_d]:
            self.speed.x += THRUST
            self.status = 'right'
            if self.rotation >= -20:
                self.rotation -= .1
        else:
            if self.rotation != 0:
                if self.rotation >0:
                    self.rotation -= .05
                if self.rotation <0:
                    self.rotation += .05
        self.speed *= 0.995
        if self.speed.magnitude() > 0: 
            self.speed.clamp_magnitude_ip(MAX_SPEED)

        
    def move(self, dt):
        print(self.speed)
        self.pos += self.speed * dt
        self.rect.center = self.pos
    def import_assests(self):
        self.animations = {'left':[], 'right':[]}
        for animation in self.animations.keys():
            full_path = './graphics/heli/' + animation
            self.animations[animation]=import_folder(full_path)
    
    def animate(self,dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

        center = self.image.get_rect().center
        self.image = pygame.transform.rotate(self.image, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
