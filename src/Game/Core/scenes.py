import pygame
from Entities.plateform import Plateform
from Entities.player import Player
from Core.events import getKeyPress
import random

class Scene:
    elements = []

    @classmethod
    def update(cls, game, events):
        for element in cls.elements.values():
            if type(element) == Player:
                getKeyPress(element)
                element.update()
                element.jump()
            if type(element) == list:
                for e in element:
                    if type(e) == Plateform:
                        e.update(cls.elements["player"], cls.elements["plateforms"])

    @classmethod
    def draw(cls, game):
        game.screen.fill((0, 0, 0)) #Supprime tout les éléments
        game.screen.blit(game.backGround, (0, 0)) #On affiche le fond

        for element in cls.elements.values():
            if type(element) == list:
                for e in element:
                    e.draw(game)
            else:
                element.draw(game)
        
        pygame.display.flip()

class GameScene(Scene):

    @classmethod
    def init(cls):
        cls.elements = {"player": Player(320, 600), "plateforms":[Plateform(random.randrange(100, 700)) for i in range(15)]}
    

class MenuScene(Scene):
    @classmethod
    def init(cls):
        cls.elements = []

class ReplayScene(Scene):
    @classmethod
    def init(cls):
        cls.elements = []