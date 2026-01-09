import pygame
from settings import WIDTH, HEIGHT, FPS
from Utils.loader import load_image
from Entities.player import Player
from Entities.plateform import Plateform, plateforms
from Core.events import getKeyPress

class Game:
    def __init__(self):
        pygame.init() #On instantie tout les modules de pygame.
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("DoodleJump")
        self.clock = pygame.time.Clock()
        self.backGround = load_image("BackGround.png") # load() stock en mémoire
        self.player = Player(320, 600)
        self.running = True


    def run(self):     #Boucle de jeu
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.clock.tick(FPS)
            getKeyPress(self.player)
            self.draw()


        pygame.quit()

    def draw(self):
        self.screen.fill((0, 0, 0)) #Supprime tout les éléments
        self.player.jump()
        self.player.update()
        self.screen.blit(self.backGround, (0, 0)) #On affiche le fond

        for i in plateforms:
            self.screen.blit( i.image_plateform, i.rect)

        self.screen.blit(self.player.imagePlayer, self.player.rect) #On affiche le joueur

        pygame.display.flip() #Permet d'afficher tout ce qui est "dessiner" en mémoire
