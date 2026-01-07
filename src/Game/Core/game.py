import pygame
from settings import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        pygame.init() #On instantie tout les modules de pygame.
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mon jeu Pygame")
        self.clock = pygame.time.Clock()
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
        self.screen.fill((0, 0, 0)) 
        pygame.display.update()
    
