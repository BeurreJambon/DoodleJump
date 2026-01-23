import pygame
import math
from Utils.loader import load_image
from Entities.bullet import Bullet
from settings import *

class Player:
    def __init__(self, x, y):
        self.imagePlayer_right = load_image("right.png")
        self.imagePlayer_left = load_image("left.png")
        self.imagePlayer_right_jump = load_image("right_jump.png")
        self.imagePlayer_left_jump = load_image("left_jump.png")
        self.imagePlayer_shoot = load_image("shoot.png")
        self.imagePlayer = self.imagePlayer_right
        self.velocity_y = 0  #Gravité
        self.velocity_x = 6
        self.jump_force = -15
        self.rect = self.imagePlayer.get_rect(midbottom = (x, y)) # x et y Donne la position de où sera placer notre image (coordonée du centre de l'image) dans la scène
        # get_rect -> Crée un rectangle exactement de la taille de l’image
        self.left_pressed = False
        self.right_pressed = False
        self.isFalling = True
        self.isGoingUp = False
        self.isjetpack = False
        self.begin_jetpack = 0

        self.can_white_platform_appears = False
        self.can_moving_platform_appears = False

        self.cooldown = 350
        self.last_animation_jump = 0
        self.last_animation_shoot = 0
        self.score = 0
        self.niveau = 0


    def update(self):
        print(self.rect.y)
        now = pygame.time.get_ticks()
        if  now - self.last_animation_shoot >= self.cooldown and self.imagePlayer == self.imagePlayer_shoot:
            self.imagePlayer = self.imagePlayer_left

        # si le cooldown est dépassé
        if (now - self.last_animation_jump >= self.cooldown) and (self.imagePlayer == self.imagePlayer_left_jump) and (now - self.last_animation_shoot >= self.cooldown):
            self.imagePlayer = self.imagePlayer_left
            #self.last_animation_jump = now

        if (now - self.last_animation_jump >= self.cooldown) and (self.imagePlayer == self.imagePlayer_right_jump) and (now - self.last_animation_shoot >= self.cooldown):
            self.imagePlayer = self.imagePlayer_right

        #si le joueur se déplace
        if self.right_pressed == True:
            self.rect.x += self.velocity_x

            if (now - self.last_animation_jump >= self.cooldown):
                self.imagePlayer = self.imagePlayer_right

            else:
                self.imagePlayer = self.imagePlayer_right_jump
        
        if self.left_pressed == True:
            self.rect.x -= self.velocity_x

            if (now - self.last_animation_jump >= self.cooldown):
                self.imagePlayer = self.imagePlayer_left

            else:
                self.imagePlayer = self.imagePlayer_left_jump

        if (now - self.last_animation_shoot <= self.cooldown):
                self.imagePlayer = self.imagePlayer_shoot
        
        if self.isjetpack == True and now - self.begin_jetpack > 4000:
            self.isjetpack = False

        self.rect.y += self.velocity_y

        if self.isjetpack == False:
            self.velocity_y += 0.35

        if self.velocity_y > 0:
            self.isFalling = True
            self.isGoingUp = False

        if self.velocity_y < 0:
            self.isGoingUp = True
            self.isFalling = False

        if self.rect.x > WIDTH:
            self.rect.x = -55

        if self.rect.x < -55:
            self.rect.x = WIDTH 
        

    def jump(self):
            self.velocity_y = self.jump_force
            self.isFalling = False
        
    def detectCollision_platform(self, platform):
        return self.rect.colliderect(platform.rect)

    def detectCollision_spring(self, spring):
        return self.rect.colliderect(spring.rect)
    
    def detectCollision_jetpack(self, jetpack):
        return self.rect.colliderect(jetpack.rect)
        
    def draw(self, game):
        game.screen.blit(self.imagePlayer, self.rect) #On affiche le joueur

    def probaWhitePlatform(self):
        if self.niveau > 25:
            self.can_white_platform_appears = True
            if self.niveau >= 127:
                return math.log(142 - 25, 1.21) / 25 / 2
            return math.log(self.niveau -25, 1.21)/ 25 /2
        return 0
        
    def probaMovingPlatform(self):
        if self.niveau > 10:
            self.can_moving_platform_appears = True 
            if self.niveau >= 125:
                return math.log(127 - 10, 1.21) / 25 / 2
            return math.log(self.niveau -10, 1.21)/ 25 /2
        return 0
    
    def shoot(self, bullets):
        now = pygame.time.get_ticks()
        self.bullet = Bullet(self.rect.x,  self.rect.y)
        bullets.append(self.bullet)
        self.imagePlayer = self.imagePlayer_shoot
        self.last_animation_shoot = now
