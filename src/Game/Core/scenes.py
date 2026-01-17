import pygame
from Entities.plateform import Plateform, MovingPlatform, Whiteplatform
from Entities.player import Player
from Entities.ui import Button, Text
from Entities.bullet import Bullet
from Core.events import getKeyPress
from settings import *
import random

class Scene:
    elements = []

    @classmethod # fonction static
    def update(cls, game, events):
        for key, element in cls.elements.items():
            if type(element) == Player:
                getKeyPress(element)
                element.update()
            if type(element) == list:
                for e in element:
                    if type(e) == Plateform or type(e) == MovingPlatform or type(e) == Whiteplatform:
                        e.update(cls.elements)
                    if type(e) == Bullet:
                        e.update(cls.elements["bullets"])
            if type(element) == Text and key == "ui":
                element.update(cls.elements["player"].score)
            if type(element) == Button:
                element.update(game, events)
                    
                        

    @classmethod
    def draw(cls, game):
        game.screen.fill((0, 0, 0)) #Supprime tout les éléments
        game.screen.blit(game.backGround, (0, 0)) #On affiche le fond
        game.screen.blit(game.topBarScore, (0, 0)) # et la barre de score

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
        cls.elements = { "plateforms":[Plateform(random.randrange(30, WIDTH - 30),random.randrange(100, 700)) for i in range(15)] + [Plateform(650, 320)], "player": Player(320, 600), "ui": Text(10, 10, "banane", 30,False), "bullets":[]}
    
    @classmethod
    def update(cls, game, events):
        super().update(game, events)
        if cls.elements["player"].rect.y > HEIGHT:
            game.scene = ReplayScene


class MenuScene(Scene):
    @classmethod
    def init(cls):
        cls.elements = {"playButton": Button(300, 400, "Assets/Image/button_play.png", GameScene), "title": Text(62, 100, "DoodleJump", 100,True)}

class ReplayScene(Scene):
    @classmethod
    def init(cls):
        cls.elements = {"menuButton": Button(300, 400, "Assets/image/button_menu.png", MenuScene), "replayButton": Button(400, 500, "Assets/Image/button_playagain.png", GameScene), "title": Text(62, 100, "DoodleJump", True)}