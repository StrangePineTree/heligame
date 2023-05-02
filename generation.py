import pygame
import random
from level import *
from settings import *
from sprites import GenericSprite
from player import *
from enemies import Enemy

enemyList: list[Enemy] = []


def GenerateObstacle(level):
    locationList = [f"./graphics/terrain features/tree{n + 1}.png" for n in range(7)]
    locationList.extend([f"./graphics/terrain features/rock{n + 1}.png" for n in range(3)])
    
    image = pygame.image.load(random.choices(locationList, [0.1, 0.5, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])[0]).convert_alpha()

    return GenericSprite(
        pos = Vector2((random.randint(2000,50000) if random.randrange(0,2) == 1 else random.randint(-50000,-1000)), SCREEN_HEIGHT-95),
        surf = image,
        groups = level.all_sprites,
        z = LAYERS['trees'],
        point = ('midbottom')
    )

    


    #randomly generate x coord

