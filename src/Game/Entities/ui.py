import pygame
from settings import WIDTH, HEIGHT

doodleFontBig = pygame.font.Font("Assets/DoodleJump.ttf", size=100)
doodleFont = pygame.font.Font("Assets/DoodleJump.ttf")

class Button:
    def __init__(self, x, y, image):
        self.coords = (x, y)
        self.image = pygame.image.load(image)
    
    def draw(self, game):
        game.screen.blit(self.image, self.coords)

class Text:
    def __init__(self, x, y, text, isBig=False):
        self.coords = (x, y)
        self.textContent = text
        self.isBig = isBig
        self.font = doodleFontBig if isBig else doodleFont
        self.render = self.font.render(self.textContent, False, pygame.Color(0, 0, 0))

    def draw(self, game):
        game.screen.blit(self.render, self.coords)

