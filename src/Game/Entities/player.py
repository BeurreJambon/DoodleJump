from Utils.loader import load_image
from settings import *

class Player:
    def __init__(self, x, y):
        self.imagePlayer_right = load_image("right_jump.png")
        self.imagePlayer_left = load_image("left_jump.png")
        self.imagePlayer = self.imagePlayer_right
        self.velocity_y = 0  #Gravité
        self.velocity_x = 6
        self.jump_force = -20
        self.rect = self.imagePlayer.get_rect(center = (x, y)) # x et y Donne la position de où sera placer le notre image (coordonée du centre de l'image) dans la scène
        # get_rect -> Crée un rectangle exactement de la taille de l’image
        self.left_pressed = False
        self.right_pressed = False


    def update(self):
        if self.right_pressed == True:
            self.rect.x += self.velocity_x
            self.imagePlayer = self.imagePlayer_right
        
        if self.left_pressed == True:
            self.rect.x -= self.velocity_x
            self.imagePlayer = self.imagePlayer_left


        self.rect.y += self.velocity_y
        self.velocity_y += 0.5

        if self.rect.x > WIDTH:
            self.rect.x = 0

        if self.rect.x < 0:
            self.rect.x = WIDTH




    def jump(self):
        if self.rect.y >= 735:
            self.velocity_y = self.jump_force
        
    def draw(self, game):
        game.screen.blit(self.imagePlayer, self.rect) #On affiche le joueur