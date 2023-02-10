import pygame
import random
from level import *
from settings import *
from sprites import GenericSprite
from player import *
from enemies import Enemy

enemyList: list[Enemy] = []


def GenerateObstacle(level):
    locationList = [
        "./graphics/terrian features/tree1.png",
        "./graphics/terrian features/tree2.png",
        "./graphics/terrian features/tree3.png",
        "./graphics/terrian features/tree4.png",
        "./graphics/terrian features/tree5.png",
        "./graphics/terrian features/tree6.png",
        "./graphics/terrian features/tree7.png",
        "./graphics/terrian features/rock1.png",
        "./graphics/terrian features/rock2.png",
        "./graphics/terrian features/rock3.png"
    ]
    
    image = pygame.image.load(random.choices(locationList, [0.1, 0.5, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])[0]).convert_alpha()

    return GenericSprite(
        pos = Vector2((random.randint(2000,50000) if random.randrange(0,2) == 1 else random.randint(-50000,-1000)), SCREEN_HEIGHT-95),
        surf = image,
        groups = level.all_sprites,
        z = LAYERS['trees'],
        point = ('midbottom')
    )

    


    #randomly generate x coord

