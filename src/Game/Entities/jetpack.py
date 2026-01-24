from Utils.loader import *
from settings import *
class Jetpack:
    def __init__(self, platform, offset_x, offset_y):
        #197 264
        sprite_sheet = load_image("game_tiles.png")
        sprite_sheet_jetpack = load_image("jetpack_tiles.png")
        self.image_jetpack_item = load_sprite(sprite_sheet, 197, 264, 26, 38)

        self.image_jetpack_animation_1 = load_sprite(sprite_sheet_jetpack, 32, 64, 32, 64)
        self.image_jetpack_animation_2 = load_sprite(sprite_sheet_jetpack,0 ,64, 32, 64 )
        self.image_jetpack_flip_1 = pygame.transform.flip(self.image_jetpack_animation_1, True, False)
        self.image_jetpack_flip_2 = pygame.transform.flip(self.image_jetpack_animation_2, True, False)

        self.last_animation_jetpack = 0
        self.cooldown = 150

        self.image_jetpack = self.image_jetpack_item
        self.platform = platform # cette ligne permet de dire : la plateform actuelle est ta plateforme et cette ligne stocke la plateforme pour pouvoir l'utiliser par la suite
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.rect = self.image_jetpack.get_rect(midbottom = (self.platform.rect.x, self.platform.rect.y))
        self.hasCollide = False

        self.frames_right = [
            self.image_jetpack_animation_1,
            self.image_jetpack_animation_2
        ]

        self.frames_left = [
            self.image_jetpack_flip_1,
            self.image_jetpack_flip_2
        ]

        self.current_frame = 0

    def update(self, player, jetpacks):
        if self.hasCollide == False:
            self.handle_collision(player, jetpacks)
            self.rect.x = self.platform.rect.x + self.offset_x 
            self.rect.y = self.platform.rect.y + self.offset_y
            

        #if self.hasCollide == True:
        else:
            self.animation_jetpack(player)

        self.remove_jetpacks(player, jetpacks)

    def handle_collision(self, player, jetpacks):
        if player.detectCollision_jetpack(self) and player.isjetpack == False and player.canCollide:
            player.begin_jetpack = pygame.time.get_ticks()
            player.velocity_y = -22
            self.hasCollide = True
            player.isjetpack = True
            self.image_jetpack = self.image_jetpack_animation_1
            
    def animation_jetpack(self, player):
        now = pygame.time.get_ticks()

        if now - self.last_animation_jetpack >= self.cooldown:
            self.current_frame = (self.current_frame + 1) % 2
            self.last_animation_jetpack = now

        # 👀 Direction du joueur
        if player.imagePlayer in (player.imagePlayer_right, player.imagePlayer_right_jump):
            self.image_jetpack = self.frames_left[self.current_frame]
            self.rect.x = player.rect.x - 7
        else:
            self.image_jetpack = self.frames_right[self.current_frame]
            self.rect.x = player.rect.x + 37

        self.rect.y = player.rect.y + 20

    def draw(self, game):
        game.screen.blit(self.image_jetpack, self.rect)

    def remove_jetpacks(self, player, jetpacks):
        if self.rect.y > HEIGHT or (self.hasCollide and player.isjetpack == False):
            jetpacks.remove(self)