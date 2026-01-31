import pygame
pygame.init() #On instantie tout les modules de pygame.

from settings import WIDTH, HEIGHT, FPS
from Utils.loader import load_image
from Entities.player import Player
from Entities.plateform import Plateform
from Entities.bullet import Bullet
from Core.events import getKeyPress
from Core.scenes import GameScene, MenuScene, ReplayScene
import random

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("DoodleJump")
        self.clock = pygame.time.Clock()
        self.backGround = load_image("BackGround.png") # load() stock en mémoire
        self.topBarScore = load_image("top_score_bar.png")

        GameScene.init()
        MenuScene.init()
        ReplayScene.init()
        self.scene = MenuScene


        self.running = True



    def run(self):     #Boucle de jeu
        while self.running:
            mousePress = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePress = event.dict["pos"]
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        GameScene.elements["player"].shoot(GameScene.elements["bullets"])


            self.clock.tick(FPS)
            self.update(mousePress)
            self.draw()


        pygame.quit()


    def update(self, events):
        self.scene.update(self, events)

    def draw(self):
        self.scene.draw(self)

    def get_input(self, player):
        velocity_x = player.velocity_x
        velocity_y = player.velocity_y
        position_y = player.rect.y
        position_x = player.rect.x

        return (velocity_x, velocity_y, position_x,  position_y)
        
