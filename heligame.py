import pygame
import sys
from settings import *
from level import Level
from generation import *
from enemies import Enemy
import cProfile
from setup import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.state = 'running'
        self.setup = Menu()
        self.num = 0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick(60) * (GAME_SPEED_MODIFIER/300)
            self.level.run(dt)
            for enemy in enemyList:
                enemy.update(self.level.player.pos)
            for attack in attacklist:
                attack.update()
                if attack.lifetime >50:
                    attack.delete = True
                if attack.delete == True:
                    attacklist.remove(attack)
            self.num += 1

            pygame.display.update()

    def menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            dt = self.clock.tick(60) * (GAME_SPEED_MODIFIER/300)
            self.setup.run()
            if self.setup.running == False:
                self.state = 'running'
                startup(self)

            pygame.display.update()
(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((comment:='hii')))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
def startup(game: Game | None = None):
    if game == None:
        game = Game()
    if game.state == 'running':
        game.run()
    elif game.state == 'menu':
        game.menu()


if __name__ == '__main__':
    if RUNTIME == True:
        cProfile.run("startup()", sort="time")
    else:
        startup()