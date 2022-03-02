import pygame
# Notre projectile par défault

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player, game):
        super().__init__()
        self.vitesse = 6
        self.player = player
        self.game = game
        self.image = pygame.image.load('assets_samourai/shuriken1.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        if self.player.p_return == False:
            self.rect.x = player.rect.x - 150
        elif self.player.p_return == True:
            self.rect.x = player.rect.x - 270
        self.rect.y = player.rect.y - 180
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle -= 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove_projectile_1(self): # Supprimer le projectile quand il sort de la fenêtre
        self.player.all_projectile1.remove(self)

    def remove_projectile_2(self):
        self.player.all_projectile2.remove(self)

    def move1(self): # On fait bouger le projectile de gauche à droite
        self.rect.x += self.vitesse
        self.rotate()
        if self.rect.x > 1080:
            self.remove_projectile_1()
            print("Projectile supprimé !")

    def move2(self):  # On fait bouger le projectile de gauche à droite
            self.rect.x -= self.vitesse
            self.rotate()
            if self.rect.x < 0:
                self.remove_projectile_2()
                print("Projectile supprimé !")
