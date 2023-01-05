import pygame
from sprites import *
from settings import *
from sprites import GenericSprite

class button:
	box: pygame.Rect
	color: pygame.Color

	def __init__(self, pos: tuple[int, int], size: tuple[int, int], color):
		self.box = pygame.Rect(pos, (size[0], size[1]))
		self.color = color


	def draw(self):
		pygame.draw.rect(pygame.display.get_surface(), self.color, self.box, 0, 8)

class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.running = True
        self.buttonList: list[button] = []
        self.startbutton = button((SCREEN_WIDTH/30,SCREEN_HEIGHT/1.3),(SCREEN_WIDTH/3,SCREEN_HEIGHT/5.3),(10,10,101))
        self.buttonList.append(self.startbutton)

        self.menuImage = pygame.image.load("./graphics/menu/bad background.png").convert_alpha()
        self.menuImage = pygame.transform.scale(self.menuImage, (SCREEN_WIDTH,SCREEN_HEIGHT)).convert_alpha()

    def run(self):
        for button in self.buttonList:
            button.draw()
        self.display_surface.fill((175, 65, 142))
        self.display_surface.blit(self.menuImage,(0,0))
        if pygame.mouse.get_pressed()[0]:
            for button in self.buttonList:
                if button.box.collidepoint(pygame.mouse.get_pos()):
                    if button is self.startbutton:
                        self.running = False
