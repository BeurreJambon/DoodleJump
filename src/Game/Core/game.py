import pygame
from settings import WIDTH, HEIGHT, FPS
from Utils.loader import load_image
from Entities.player import Player
from Entities.plateform import Plateform
from Core.events import getKeyPress
from Core.scenes import GameScene, MenuScene, ReplayScene
import random

class Game:
    def __init__(self):
        pygame.init() #On instantie tout les modules de pygame.
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("DoodleJump")
        self.clock = pygame.time.Clock()
        self.backGround = load_image("BackGround.png") # load() stock en mémoire

        GameScene.init()
        MenuScene.init()
        ReplayScene.init()
        self.scene = GameScene

        self.running = True



    def run(self):     #Boucle de jeu
        while self.running:
            mousePress = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePress = event.dict["pos"]


            self.clock.tick(FPS)
            self.update(mousePress)
            self.draw()


        pygame.quit()


    def update(self, events):
        self.scene.update(self, events)

    def draw(self):
        self.scene.draw(self)
