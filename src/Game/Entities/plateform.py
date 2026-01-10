from Utils.loader import load_image, load_sprite
from settings import *
import random

class Plateform:
    def __init__(self, y = 600):
        self.sprite_sheet = load_image("game_tiles.png")
        self.image_plateform = load_sprite(self.sprite_sheet, 0, 0 , 60, 16)
        self.rect = self.image_plateform.get_rect(center = (random.randrange(30, WIDTH - 30), y))
        self.isOnPlateform = False

    def update(self, player):
        if player.isGoingUp and player.rect.y <= 300:
            self.rect.y -= player.velocity_y
            player.rect.y = 300

    def addPlatform(self):
        if (plateforms[-1].rect.y >= 0):
            self.plateform = Plateform(random.randint(-70, -60))
            plateforms.append(self.plateform)

    def deletePlatform(self):
        if self.rect.y > HEIGHT:
            plateforms.remove(self)
    


    def draw(self, game):
        game.screen.blit( self.image_plateform, self.rect)