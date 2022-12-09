import pygame
#o,[prt]
import math
from settings import *
from support import *
from pygame.math import Vector2
from weapons import *
from level import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assests()

        self.status = 'right'
        self.frame_index = 0

        self.image = self.animations[self.status]
        self.z = LAYERS['main']

        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed: Vector2 = Vector2(0, 0)
        self.rotation = 0
        self.thrust = 16
        self.missileCD = 0

        self.scroll:Vector2 = Vector2(0,0)
        self.scrollParralax:Vector2 = Vector2(0,0)

        self.display_surface = pygame.display.get_surface()

    def input(self):
        keys = pygame.key.get_pressed()

        offset:Vector2 = Vector2(self.pos.x - SCREEN_WIDTH / 2,self.pos.y - SCREEN_HEIGHT / 2)
        if pygame.mouse.get_pressed()[0]:
            if self.missileCD <= 0:
                attacklist.append(Missile(self.pos,(5 * MISSILE_SPEAD),True,pygame.mouse.get_pos()+offset))
                self.missileCD = MISSILE_COOLDOWN
        if keys[pygame.K_w]:
            if self.thrust < MAX_THRUST:
                self.thrust += .025
        elif keys[pygame.K_s]:
            if self.thrust > 0:
                self.thrust -= .025
        if keys[pygame.K_a]:
            self.rotation += .25 * TURN_SPEED
        elif keys[pygame.K_d]:
            self.rotation -= .25 * TURN_SPEED
        else:
            pass

        
    def move(self, dt):
        self.speed.y -= math.cos(math.radians(self.rotation)) * SPEED_MULTIPLIER * self.thrust * dt / 4
        self.speed.x -= math.sin(math.radians(self.rotation)) * SPEED_MULTIPLIER * self.thrust * dt / 4
        self.pos += self.speed
        self.speed *=0.99
        self.speed.y+=dt * 4 * GRAVITY

        self.scroll -= self.speed
        self.scrollParralax -= self.speed / PARALLAX_FACTOR*.2

        if self.speed.x > 0:
            self.status = 'right'
        if self.speed.x < 0:
            self.status = 'left'

        if self.pos.y <-50000:
            self.speed.y += 10

        self.missileCD -= 1


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

    def displayGUI(self):
        pygame.draw.rect(self.display_surface, (100,200,100),[SCREEN_WIDTH-60,SCREEN_HEIGHT-260,50,250])
        pygame.draw.rect(self.display_surface, (100,200,100),[20,10,150,20])
        pygame.draw.rect(self.display_surface, (100,200,100),[+20,SCREEN_HEIGHT-220,200,200])
        self.updateGUI()
        
    def updateGUI(self):
        pass
    #will update GUI elements here

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
