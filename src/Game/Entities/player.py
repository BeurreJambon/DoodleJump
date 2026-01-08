from Utils.loader import load_image

class Player:
    def __init__(self, x, y):
        self.imagePlayer = load_image("right_jump.png")
        self.velocity_y = 0  #Gravité
        self.rect = self.imagePlayer.get_rect(center = (x, y)) # x et y Donne la position de où sera placer le notre image (coordonée du centre de l'image) dans la scène
        # get_rect -> Crée un rectangle exactement de la taille de l’image

    def Update(self):
        self.velocity_y += 0.0
        self.rect.y += self.velocity_y