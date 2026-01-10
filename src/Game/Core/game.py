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
        self.startGame()



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
            print(len(plateforms))


        pygame.quit()


    def update(self, events):
        self.scene.update(self, events)

    def draw(self):
        self.screen.fill((0, 0, 0)) #Supprime tout les éléments
        self.player.update()
        self.screen.blit(self.backGround, (0, 0)) #On affiche le fond

        for i in plateforms:
            #i.detectCollision(self.player)
            #i.update(self.player)
            i.update(self.player)
            i.addPlatform()
            self.screen.blit( i.image_plateform, i.rect)
            if (self.player.detectCollision(i) or self.player.rect.y > HEIGHT) and self.player.isFalling:
                self.player.jump()
            i.deletePlatform()

        self.screen.blit( self.plateform.image_plateform, self.plateform.rect)
        self.screen.blit(self.player.imagePlayer, self.player.rect) #On affiche le joueur
        pygame.display.flip() #Permet d'afficher tout ce qui est "dessiner" en mémoire

    def startGame(self):
        for i in range(15):
            self.plateform = Plateform(random.randrange(100, 700))
            plateforms.append(self.plateform)