import pygame
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
ASSET_PATH = os.path.join(BASE_PATH, "Assets", "Image")

def load_image(image):
    imageFound = os.path.join(ASSET_PATH, image)
    return pygame.image.load(imageFound).convert_alpha()
    