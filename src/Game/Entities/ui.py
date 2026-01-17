import pygame
from settings import WIDTH, HEIGHT
from Utils.loader import define_font

doodleFontBig = pygame.font.Font("Assets/DoodleJump.ttf", size=100)
doodleFontScore = pygame.font.Font("Assets/DoodleJump.ttf", size=100)
doodleFont = pygame.font.Font("Assets/DoodleJump.ttf")

class Button:
    def __init__(self, x, y, image, sceneChange):
        self.coords = (x, y)
        self.image = pygame.image.load(image)
        self.dimensions = self.image.get_clip()
        self.dimensions.x, self.dimensions.y = self.coords

        self.scene = sceneChange # C'est la scène sur laquelle on change quand on appuie sur le bouton.
    
    def update(self, game, mouse):
        if mouse == None:
            return
        if self.dimensions.collidepoint(mouse):
            game.scene = self.scene
            game.scene.init()
    
    def draw(self, game):
        game.screen.blit(self.image, self.coords)

class Text:
    def __init__(self, x, y, text, size ,isBig=False, isScore=False):
        self.coords = (x, y)
        self.textContent = text
        self.isBig = isBig
        self.isScore = isScore # On veut savoir si c'est le score pour update
        self.font = define_font("Assets/DoodleJump.ttf", size) #doodleFontBig if isBig else doodleFont
        self.render = self.font.render(self.textContent, False, pygame.Color(0, 0, 0))

    def draw(self, game):
        game.screen.blit(self.render, self.coords)

    def update(self, elements):  
        if self.isScore:      
            self.textContent = str(elements["player"].score)
            self.render = self.font.render(self.textContent, False, pygame.Color(0, 0, 0))
