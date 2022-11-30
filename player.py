import pygame
#o,[prt]
import math
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
        self.thrust = 16

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.thrust < MAX_THRUST:
                self.thrust += .01
        elif keys[pygame.K_s]:
            if self.thrust > 0:
                self.thrust -= .01
        if keys[pygame.K_a]:
            self.rotation += .25
        elif keys[pygame.K_d]:
            self.rotation -= .25
        else:
            pass

        
    def move(self, dt):
        self.speed.y -= math.cos(math.radians(self.rotation)) * SPEED_MULTIPLIER * self.thrust * dt
        self.speed.x -= math.sin(math.radians(self.rotation)) * SPEED_MULTIPLIER * self.thrust * dt
        self.pos += self.speed
        self.speed *=0.99
        self.speed.y+=dt * GRAVITY
        print(self.thrust)

    #gravity always pulls down at strenth of 30
    #thrust is added to that
    #if thrust is 0, gravity grows
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
        self.z = LAYERS['main']

        center = self.image.get_rect().center
        self.image = pygame.transform.rotate(self.image, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
