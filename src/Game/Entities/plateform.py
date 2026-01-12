from Utils.loader import load_image, load_sprite
from settings import *
import random
import pygame

class Plateform:
    def __init__(self, y = 600, x = random.randrange(30, WIDTH - 30)):
        self.sprite_sheet = load_image("game_tiles.png")
        self.image_plateform = load_sprite(self.sprite_sheet, 0, 0 , 60, 16)
        self.rect = self.image_plateform.get_rect(center = (x, y))
        self.isOnPlateform = False

    def update(self, player, plateformsList):
        if player.isGoingUp and player.rect.y <= 300:
            self.rect.y -= player.velocity_y
            player.rect.y = 300
            player.score += 1

    
        if (plateformsList[-1].rect.y >= 0):
            self.plateform = Plateform(random.randint(-70, -60), random.randrange(30, WIDTH - 30))
            plateformsList.append(self.plateform)
        
        if player.detectCollision(self) and player.isFalling and player.rect.bottom <= self.rect.top + 15:
                player.rect.bottom = self.rect.top
                player.jump()
                now = pygame.time.get_ticks()

                if player.imagePlayer == player.imagePlayer_right:
                    player.imagePlayer = player.imagePlayer_right_jump
                    player.last_animation_jump = now

                if player.imagePlayer == player.imagePlayer_left:
                    player.imagePlayer = player.imagePlayer_left_jump
                    player.last_animation_jump = now

        if self.rect.y > HEIGHT:
            plateformsList.remove(self)

    def draw(self, game):
        game.screen.blit( self.image_plateform, self.rect)