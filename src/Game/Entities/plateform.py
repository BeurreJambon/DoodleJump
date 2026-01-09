from Utils.loader import load_image, load_sprite
import random

plateforms = []

class Plateform:
    def __init__(self):
        self.sprite_sheet = load_image("game_tiles.png")
        self.image_plateform = load_sprite(self.sprite_sheet, 0, 0 , 60, 16)
        self.rect = self.image_plateform.get_rect(center = ( random.randrange(0,640), 700))

    def createPlateform(self):
        self.plateform = Plateform()
        plateforms.append(self.plateform)