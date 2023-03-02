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
        self.helitype = HELITYPE
        self.import_assests()

        self.handle = pygame.image.load("./graphics/GUI/throttle handle.png").convert_alpha()
        self.needle = pygame.image.load("./graphics/GUI/speedometer needle.png").convert_alpha()
        self.numbers = pygame.image.load("./graphics/GUI/speedometer numbers.png").convert_alpha() #ToDo: draw these
        self.speedometer = pygame.image.load("./graphics/GUI/speedometer.png").convert_alpha()

        self.status = 'right'
        self.frame_index = 0

        self.image = self.animations[self.status]
        self.z = LAYERS['player']

        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = pygame.rect.Rect(SCREEN_WIDTH/2-64,SCREEN_HEIGHT/2-30,128,60)

        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed: Vector2 = Vector2(0, 0)
        self.rotation = 0
        self.thrust = 5
        self.missileCD = 0
        self.hp = 1000
        self.flares = 100
        self.flare = False
        self.fall = True
        self.mouseAngle = 0

        if HELITYPE == 'transport':
            self.gunright = pygame.image.load("./graphics/heli/transport/gun(left).png").convert_alpha()
            self.gunleft = pygame.image.load("./graphics/heli/transport/gun(right).png").convert_alpha()
            self.gun = self.gunright

        self.scroll:Vector2 = Vector2(0,0)
        self.scrollParralax:Vector2 = Vector2(0,0)

        self.display_surface = pygame.display.get_surface()

        self.ඞ = 'sus'

    def input(self):
        keys = pygame.key.get_pressed()

        offset:Vector2 = Vector2(self.pos.x - SCREEN_WIDTH / 2,self.pos.y - SCREEN_HEIGHT / 2)
        self.mouseAngle = math.degrees(math.atan2(pygame.mouse.get_pos()[1]+offset.y-self.pos.y,pygame.mouse.get_pos()[0]+offset.x-self.pos.x))
        print(self.mouseAngle)
        if pygame.mouse.get_pressed()[0] and self.helitype == 'transport':
            if self.missileCD <= 0:
                attacklist.append(Bullet(self.pos,(75 * ATTACK_SPEED),True,pygame.mouse.get_pos()+offset))
                self.missileCD = ATTACK_COOLDOWN * 10

        if pygame.mouse.get_pressed()[0] and self.helitype == 'basic':
            if self.missileCD <= 0:
                attacklist.append(Missile(self.pos,(10 * ATTACK_SPEED),True,pygame.mouse.get_pos()+offset))
                self.missileCD = ATTACK_COOLDOWN * 75

        if keys[pygame.K_w]:
            if self.thrust < MAX_THRUST:
                self.thrust += .05
        elif keys[pygame.K_s]:
            if self.thrust > 0:
                self.thrust -= .05
        if keys[pygame.K_a]:
            self.rotation += .25 * (3*TURN_SPEED)
        elif keys[pygame.K_d]:
            self.rotation -= .25 * (3*TURN_SPEED)
        else:
            pass

        
    def move(self, dt):
        self.speed.y -= math.cos(math.radians(self.rotation)) * SPEED_MULTIPLIER * self.thrust * dt / 4
        self.speed.x -= math.sin(math.radians(self.rotation)) * SPEED_MULTIPLIER * self.thrust * dt / 4
        self.speed *=0.99
        if self.fall == True:
            self.speed.y+=dt * GRAVITY
        self.scrollParralax -= self.speed / PARALLAX_FACTOR*.2
        self.scroll -= self.speed
        if self.pos.y > SCREEN_HEIGHT-100 and self.speed.y > 0:
            pass
        else:
            self.pos += self.speed
        if self.speed.x > 0: #todo: change this to use self.rotation
            self.status = 'right'
        if self.speed.x < 0:
            self.status = 'left'
        if self.pos.y <-50000:
            self.speed.y += 10

        self.missileCD -= 1

    def crash(self,speed:Vector2, rotation):
        self.speed.x /= 1.1
        self.speed.y *= .7
        if self.speed.y > 0:
            self.speed.y = -abs(self.speed.y)
        
    #maybe make this completly scripted, basicly put the player in a cut scene

    def collide(self,scroll):
        #rotate self.hitbox
        #use self.hitbox for missiles, attacks, ect
        for attack in attacklist:
            if self.hitbox.colliderect(attack.hitbox):
                self.hp -= attack.damage
                attacklist.remove(attack)
                print('hit')

        if self.rect.bottom-20 > SCREEN_HEIGHT-100:
            self.crash(self.speed, self.rotation)
            self.fall = False
            if self.speed.y < .5:
                self.speed.y = 0
        elif self.pos.y < SCREEN_HEIGHT-101:
            self.fall = True
            #do heavy damage to the player based on speed here
            #make a better 'crash', make player spin and flip around before dying (they should have flown better)

    def import_assests(self):
        full_path = ''
        self.animations: dict[str, list[pygame.Surface]] = {'left':[], 'right':[]}
        for animation in self.animations.keys():
            if self.helitype == 'transport':
                full_path = './graphics/heli/transport/' + animation
            else:
                full_path = './graphics/heli/bad heli/' + animation
            self.animations[animation]=(((import_folder((((full_path)))))))
    
    def animate(self,dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
        self.z = LAYERS['player']

        center = self.image.get_rect().center
        self.image = pygame.transform.rotate(self.image, self.rotation)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


    def displayGUI(self):
        pygame.draw.rect(self.display_surface, (00,200,200),[SCREEN_WIDTH-60,SCREEN_HEIGHT-260,50,250])#throttle
        needle = pygame.transform.rotate(self.needle, 115-(self.speed.length() * 9))#IMPORTANT: this code rotates around center (1/3)
        self.needleRect = needle.get_rect(center = self.needle.get_rect(center = (120,SCREEN_HEIGHT-120)).center)#IMPORTANT: this code rotates around center (2/3)
        pygame.draw.rect(self.display_surface, (100,100,200),[20,10,150,20])

        self.handleStartPos = SCREEN_HEIGHT/1.04 - (self.thrust * 15.5)
        self.display_surface.blit(self.handle,(SCREEN_WIDTH-60,self.handleStartPos))
        self.display_surface.blit(self.speedometer,(+20,SCREEN_HEIGHT-220))
        self.display_surface.blit(needle,(self.needleRect))#todo: remove magic numbers #IMPORTANT: this code rotates around center (3/3)
        self.display_surface.blit(self.numbers,(20,SCREEN_HEIGHT-220))

        if HELITYPE == "transport":
            if abs(self.mouseAngle) > 90:
                gun = self.gunleft
            else:
                gun = self.gunright
            gun = pygame.transform.rotate(gun,-self.mouseAngle)
            self.gunrect = gun.get_rect(center = self.gun.get_rect(center = (640, SCREEN_HEIGHT-130)).center)
            self.gunrect.center = self.rect.center
            self.display_surface.blit(gun, self.gunrect)

    def update(self, dt):
        self.input()
        self.collide(self.scroll)
        self.move(dt)
        self.animate(dt)
