import pygame
import sys
from settings import *
from level import Level
from generation import *
from enemies import Enemy
import cProfile

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick()/(1000 * 1/GAME_SPEED_MODIFIER)
            self.level.run(dt)
            pygame.display.update()
            for enemy in enemyList:
                enemy.update()
            for attack in attacklist:
                attack.update()
                if attack.delete == True:
                    attacklist.remove(attack)

if __name__ == '__main__':
    game = Game()
    game.run()
    if RUNTIME == True:
        cProfile.run("game.run()", sort="time")