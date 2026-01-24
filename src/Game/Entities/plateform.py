from Utils.loader import load_image, load_sprite
from Entities.spring import Spring
from Entities.jetpack import Jetpack
from settings import *
import random
import pygame
import math

class Plateform:
    def __init__(self, y = 600, x = random.randrange(30, WIDTH - 30), y_sprite_sheet = 0):
        self.sprite_sheet = load_image("game_tiles.png")
        self.y_spriteSheet = y_sprite_sheet
        self.image_plateform = load_sprite(self.sprite_sheet, 1, self.y_spriteSheet, 58, 16)
        self.rect = self.image_plateform.get_rect(center = (x, y))
        self.isOnPlateform = False
        self.hasJump = False

    def update(self, elements):
        self.handle_scroll(elements["player"])
        self.handle_collision(elements["player"])
        self.delete_platform(elements["plateforms"])

    def handle_scroll(self,player):
        if player.isGoingUp and player.rect.y <= 300:
            self.rect.y -= player.velocity_y
            player.rect.y = 300
            player.score += 1
            if (player.score >= player.niveau * 1000):
                 player.niveau += 1

    def handle_collision(self, player):
        if player.detectCollision_platform(self) and player.isFalling and player.rect.bottom <= self.rect.top + 15 and player.canCollide:
            player.rect.bottom = self.rect.top
            player.jump()
            self.hasJump = True
            now = pygame.time.get_ticks()
            if player.imagePlayer == player.imagePlayer_right:
                player.imagePlayer = player.imagePlayer_right_jump
                player.last_animation_jump = now
            if player.imagePlayer == player.imagePlayer_left:
                    player.imagePlayer = player.imagePlayer_left_jump
                    player.last_animation_jump = now

    def delete_platform(self, plateformsList):
            if self.rect.y > HEIGHT + 40:
                plateformsList.remove(self)

    def draw(self, game):
        game.screen.blit(self.image_plateform, self.rect)

class MovingPlatform(Plateform):
        def __init__(self, y = 600, x = random.randrange(30, WIDTH - 30)):
            super().__init__(y, x, y_sprite_sheet = 19)
            self.speed = 2 

        def update(self, elements):
            super().update(elements)  # logique de base
            self.move()

        def move(self):
            self.rect.x += self.speed
            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.speed *= -1

class Whiteplatform(Plateform):
     def __init__(self, y = 600, x = random.randrange(30, WIDTH - 30)):
          super().__init__(y, x, y_sprite_sheet = 55)

     def update(self, elements):
        super().update(elements)  # logique de base
        if self.hasJump:
            elements["plateforms"].remove(self)