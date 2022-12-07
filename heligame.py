import pygame
import sys
from settings import *
from level import Level
from generation import *
from enemies import Enemy

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
            dt = self.clock.tick()/750
            self.level.run(dt)
            pygame.display.update()
            for enemy in enemyList:
                enemy.update()
            for attack in atttacklist:
                print('aa')
                attack.update

if __name__ == '__main__':
    game = Game()
    game.run()