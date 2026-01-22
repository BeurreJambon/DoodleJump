from Utils.loader import load_image, load_sprite
from Entities.spring import Spring
from Entities.jetpack import Jetpack
from settings import *
import random
import pygame
import math

class Plateform:
    spawnChanceSpring = 0.12
    spawnChanceJetpacks = 0.01
    position_platform_y = -70


    def __init__(self, y = 600, x = random.randrange(30, WIDTH - 30), y_sprite_sheet = 0):
        self.sprite_sheet = load_image("game_tiles.png")
        self.y_spriteSheet = y_sprite_sheet
        self.image_plateform = load_sprite(self.sprite_sheet, 1, self.y_spriteSheet, 58, 16)
        self.rect = self.image_plateform.get_rect(center = (x, y))
        self.isOnPlateform = False
        self.hasJump = False
        self.decay = 0.9999


    def update(self, elements):
        self.handle_scroll(elements["player"])
        self.create_new_platform(elements["plateforms"], elements["player"], elements["springs"], elements["jetpacks"])
        self.handle_collision(elements["player"])
        self.delete_platform(elements["plateforms"])



        print(Plateform.position_platform_y)


    def handle_scroll(self,player):
        if player.isGoingUp and player.rect.y <= 300:
            self.rect.y -= player.velocity_y
            player.rect.y = 300
            player.score += 1

            if (player.score >= player.niveau * 1000):
                 player.niveau += 1

                      
    
    def create_new_platform(self, plateformsList, player, springs, jetpacks):
        if (plateformsList[-1].rect.y >= 0):
            self.choose_platform(plateformsList, player, springs, jetpacks)



    def handle_collision(self, player):
        if player.detectCollision_platform(self) and player.isFalling and player.rect.bottom <= self.rect.top + 15:
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

    def choose_platform(self, plateformsList, player, springs, jetpacks):
            r = random.random()
            randomSpring = random.random()
            randomJetpack = random.random()
            
            if  r <= player.probaMovingPlatform():
                self.plateform = MovingPlatform(random.uniform(Plateform.position_platform_y, -70.0), random.randrange(30, WIDTH - 30))

                if randomSpring <= Plateform.spawnChanceSpring:
                    spring = Spring(self.plateform, 20, -10)
                    springs.append(spring)

                elif randomJetpack <= Plateform.spawnChanceJetpacks:
                     jetpack = Jetpack(self.plateform, 20, -35)
                     jetpacks.append(jetpack)
                     
            elif r <= player.probaMovingPlatform() + player.probaWhitePlatform():
                self.plateform = Whiteplatform(random.uniform(Plateform.position_platform_y, -70.0), random.randrange(30, WIDTH - 30))

                if randomJetpack <= Plateform.spawnChanceJetpacks:
                     jetpack = Jetpack(self.plateform, 20, -35)
                     jetpacks.append(jetpack)


            else:
                 self.plateform = Plateform(random.uniform(Plateform.position_platform_y, -70.0), random.randrange(30, WIDTH - 30))

                 if randomSpring <= Plateform.spawnChanceSpring:
                    spring = Spring(self.plateform, 20, -10)
                    springs.append(spring)

                 elif randomJetpack <= Plateform.spawnChanceJetpacks:
                     jetpack = Jetpack(self.plateform, 20, -35)
                     jetpacks.append(jetpack)
            
           # spring = Spring(self.plateform, 20, -10)
           # springs.append(spring)


            
            plateformsList.append(self.plateform)

            if Plateform.spawnChanceJetpacks > 0.005:
                Plateform.spawnChanceJetpacks *= self.decay
            
            if Plateform.spawnChanceSpring > 0.08:
                 Plateform.spawnChanceSpring *= self.decay

            if Plateform.position_platform_y >= -300:
                Plateform.position_platform_y -= 0.1

    def draw(self, game):
        game.screen.blit(self.image_plateform, self.rect)

class MovingPlatform(Plateform):
        def __init__(self, y = 600, x = random.randrange(30, WIDTH - 30)):
            super().__init__(y, x, y_sprite_sheet = 19)
            self.speed = 2 
            #
            #self.image_plateform = load_sprite(self.sprite_sheet, 0, 19 , 60, 16)
            #self.rect = self.image_plateform.get_rect(center = (x, y))

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
