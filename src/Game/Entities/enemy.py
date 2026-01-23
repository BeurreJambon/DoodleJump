from Utils.loader import *

class Enemy:
    def __init__(self):
         sprite_sheet = load_image("game_tiles.png")
         self.image_Enemy_1 = load_sprite(sprite_sheet, 64, 180, 38, 52)
         self.image_Enemy_2 = load_sprite(sprite_sheet, 64, 180, 38, 52)
         self.image_Enemy = self.image_Enemy_1
         self.rect = self.image_Enemy.get_rect(center = (100, 100))

    def update(self):
         pass
    
    def draw(self, game):
         game.screen.blit(self.image_Enemy, self.rect)