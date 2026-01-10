from Utils.loader import load_image, load_sprite
from settings import *
import random

plateforms = []

class Plateform:
    def __init__(self):
        self.sprite_sheet = load_image("game_tiles.png")
        self.image_plateform = load_sprite(self.sprite_sheet, 0, 0 , 60, 16)
        self.rect = self.image_plateform.get_rect(center = (random.randrange(30, WIDTH - 30), 500))
    
    def detectCollision(self, joueur):
        if joueur.rect.colliderect(self.rect):
            print(123)