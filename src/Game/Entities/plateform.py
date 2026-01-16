from Utils.loader import load_image, load_sprite
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


    def update(self, player, plateformsList):
        self.handle_scroll(player)
        self.create_new_platform(plateformsList, player)
        self.handle_collision(player)
        self.delete_platform(plateformsList)

    def handle_scroll(self,player):
        if player.isGoingUp and player.rect.y <= 300:
            self.rect.y -= player.velocity_y
            player.rect.y = 300
            player.score += 1

            if (player.score >= player.niveau * 1000):
                 player.niveau += 1
                 print(player.niveau)

                      
    
    def create_new_platform(self, plateformsList, player):
        if (plateformsList[-1].rect.y >= 0):
            self.choose_platform(plateformsList, player)


    def handle_collision(self, player):
        if player.detectCollision(self) and player.isFalling and player.rect.bottom <= self.rect.top + 15:
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
            if self.rect.y > HEIGHT:
                plateformsList.remove(self)

    def choose_platform(self, plateformsList, player):
            r = random.random()
            #if self.niveau -10 > 0: 
            
            if  r <= player.probaMovingPlatform():
                self.plateform = MovingPlatform(random.randint(-70, -60), random.randrange(30, WIDTH - 30))

            elif r <= player.probaMovingPlatform() + player.probaWhitePlatform():
                self.plateform = Whiteplatform(random.randint(-70, -60), random.randrange(30, WIDTH - 30))

            else:
                 self.plateform = Plateform(random.randint(-70, -60), random.randrange(30, WIDTH - 30))
                 
                 
            plateformsList.append(self.plateform)

    def draw(self, game):
        game.screen.blit(self.image_plateform, self.rect)

class MovingPlatform(Plateform):
        def __init__(self, y = 600, x = random.randrange(30, WIDTH - 30)):
            super().__init__(y, x, y_sprite_sheet = 19)
            self.speed = 2 
            #
            #self.image_plateform = load_sprite(self.sprite_sheet, 0, 19 , 60, 16)
            #self.rect = self.image_plateform.get_rect(center = (x, y))

        def update(self, player, plateformsList):
            super().update(player, plateformsList)  # logique de base
            self.move()

        def move(self):
            self.rect.x += self.speed
            if self.rect.left <= 0 or self.rect.right >= WIDTH:
                self.speed *= -1

class Whiteplatform(Plateform):
     def __init__(self, y = 600, x = random.randrange(30, WIDTH - 30)):
          super().__init__(y, x, y_sprite_sheet = 55)

     def update(self, player, plateformsList):
        super().update(player, plateformsList)  # logique de base
        if self.hasJump:
             plateformsList.remove(self)
