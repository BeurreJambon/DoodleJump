from Utils.loader import load_image
from settings import *
import pygame

class Player:
    def __init__(self, x, y):
        self.imagePlayer_right = load_image("right.png")
        self.imagePlayer_left = load_image("left.png")
        self.imagePlayer_right_jump = load_image("right_jump.png")
        self.imagePlayer_left_jump = load_image("left_jump.png")
        self.imagePlayer = self.imagePlayer_right
        self.velocity_y = 0  #Gravité
        self.velocity_x = 6
        self.jump_force = -15
        self.rect = self.imagePlayer.get_rect(midbottom = (x, y)) # x et y Donne la position de où sera placer le notre image (coordonée du centre de l'image) dans la scène
        # get_rect -> Crée un rectangle exactement de la taille de l’image
        self.left_pressed = False
        self.right_pressed = False
        self.isFalling = True
        self.isGoingUp = False

        self.cooldown = 250
        self.last_animation_jump = 0



    def update(self):

        now = pygame.time.get_ticks()
 

        if (now - self.last_animation_jump >= self.cooldown) and (self.imagePlayer == self.imagePlayer_left_jump):
            self.imagePlayer = self.imagePlayer_left
            print(type(self.last_animation_jump))
            #self.last_animation_jump = now

        if (now - self.last_animation_jump >= self.cooldown) and (self.imagePlayer == self.imagePlayer_right_jump):
            self.imagePlayer = self.imagePlayer_right
            print(type(self.last_animation_jump))

            #self.last_animation_jump = now
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


        self.rect.y += self.velocity_y
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
        
    def detectCollision(self, platform):
        return self.rect.colliderect(platform.rect)
        
    def draw(self, game):
        game.screen.blit(self.imagePlayer, self.rect) #On affiche le joueur
        