import pygame

def getKeyPress(player):    
    keys = pygame.key.get_pressed()

    player.left_pressed = keys[pygame.K_LEFT]
    player.right_pressed = keys[pygame.K_RIGHT]