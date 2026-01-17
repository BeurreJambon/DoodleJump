from Utils.loader import load_image

class Bullet:
    def __init__(self, x, y):
        self.image_bullet = load_image("projectile.png")
        self.rect = self.image_bullet.get_rect(midtop = (x +30, y))
        self.velocity = 15

    def update(self, listBullets):
        self.rect.y -= self.velocity      

        if self.rect.y < 0:
            self.deleteBullet(listBullets)

    def draw(self, game):
        game.screen.blit(self.image_bullet, self.rect)

    def deleteBullet(self, listBullets):
        listBullets.remove(self)


