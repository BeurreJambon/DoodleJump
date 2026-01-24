from settings import *
from Utils.loader import *
from Entities.bullet import Bullet

class Enemy:
    def __init__(self):
         sprite_sheet = load_image("game_tiles.png")
         self.image_Enemy_1 = load_sprite(sprite_sheet, 64, 182, 39, 56)
         self.image_Enemy_2 = load_sprite(sprite_sheet, 105, 182, 39, 56)
         self.image_Enemy = self.image_Enemy_1
         self.rect = self.image_Enemy.get_rect(center = (200, - 60))
         self.velocity = 4

    def update(self, bullets, enemies, player):
         self.handle_scroll(player)
         if self.rect.x > WIDTH - 30 or self.rect.x < 0:
            self.velocity *= -1
            if self.image_Enemy == self.image_Enemy_1:
                self.image_Enemy = self.image_Enemy_2
            else:
                self.image_Enemy = self.image_Enemy_1
        

         self.rect.x += self.velocity
         self.Collision(bullets, enemies, player)
    
    def draw(self, game):
         game.screen.blit(self.image_Enemy, self.rect)

    def Collision(self, bullets, enemies, player):
         for bullet in bullets:
            if bullet.detectCollision(self):
                enemies.remove(self)

         if player.detectCollision_enemy(self):
            player.canCollide = False

    def handle_scroll(self, player):
        if player.isGoingUp and player.rect.y <= 300:
            self.rect.y -= player.velocity_y

        