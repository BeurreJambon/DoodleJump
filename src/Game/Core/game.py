import pygame
from settings import WIDTH, HEIGHT, FPS
from Utils.loader import load_image
from Entities.player import Player

class Game:
    def __init__(self):
        pygame.init() #On instantie tout les modules de pygame.
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("DoodleJump")
        self.clock = pygame.time.Clock()
        self.backGround = load_image("BackGround.png")
        self.player = Player(320, 600)
        self.running = True


    def run(self):     #Boucle de jeu
        while self.running:
            #print("le jeu est lancé")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.clock.tick(FPS)
            self.draw()

        pygame.quit()

    def draw(self):
        self.screen.fill((0, 0, 0)) #Supprime tout les éléments

        self.player.Update()
        self.screen.blit(self.backGround, (0, 0))
        self.screen.blit(self.player.imagePlayer, self.player.rect)
        pygame.display.flip()

    
