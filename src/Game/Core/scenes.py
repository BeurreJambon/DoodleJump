import pygame
from Entities.plateform import Plateform
from Entities.player import Player
from Core.events import getKeyPress

class Scene:
    elements = []

    @classmethod
    def update(cls, game, events):
        for element in cls.elements:
            if type(element) == Player:
                getKeyPress(element)
                element.update()
                element.jump()

    @classmethod
    def draw(cls, game):
        game.screen.fill((0, 0, 0)) #Supprime tout les éléments
        game.screen.blit(game.backGround, (0, 0)) #On affiche le fond

        for element in cls.elements:
            element.draw(game)
        
        pygame.display.flip()

class GameScene(Scene):

    @classmethod
    def init(cls):
        cls.elements = [Player(320, 600), Plateform()]
    

class MenuScene(Scene):
    @classmethod
    def init(cls):
        cls.elements = []

class ReplayScene(Scene):
    @classmethod
    def init(cls):
        cls.elements = []