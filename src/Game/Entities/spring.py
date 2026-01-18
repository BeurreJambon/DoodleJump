from Utils.loader import *
from settings import *

class Spring:
    def __init__(self, platform, offset_x, offset_y):
        sprite_sheet = load_image("game_tiles.png")
        self.image_spring_1 = load_sprite(sprite_sheet, 403, 98, 20, 16)
        self.image_spring_2 = load_sprite(sprite_sheet, 403 , 114, 20, 25)
        self.image_spring = self.image_spring_1
        self.platform = platform
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.rect = self.image_spring_1.get_rect(midbottom = (self.platform.rect.x, self.platform.rect.y))

    def draw(self, game):
        game.screen.blit(self.image_spring, self.rect)

    def update(self, player, springs):
        self.handle_collision(player)
        self.rect.x = self.platform.rect.x + self.offset_x
        self.rect.y = self.platform.rect.y + self.offset_y
        self.deleteSpring(springs)

    def handle_collision(self, player):
        if player.detectCollision_spring(self) and player.isFalling:
            player.jump_force = -23
            player.jump()
            player.jump_force = -15
            self.image_spring = self.image_spring_2

    def deleteSpring(self, springs):
        if self.rect.y > HEIGHT:
            springs.remove(self)