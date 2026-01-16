import pygame
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
ASSET_PATH = os.path.join(BASE_PATH, "Assets", "Image")

def load_image(image):
    imageFound = os.path.join(ASSET_PATH, image)
    return pygame.image.load(imageFound).convert_alpha()

def load_sprite(sprite_sheet, x, y, width, height):
    sprite = sprite_sheet.subsurface((x, y, width, height))
    return sprite.copy()  #copy() permet de créer une vrai image indépendante du sprite sheet

def define_font(font, size):
    return pygame.font.Font(font, size)