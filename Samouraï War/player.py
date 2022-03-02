import pygame
from projectile import Projectile

# Le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.vitesse = 5
        self.player = Player
        self.all_projectile1 = pygame.sprite.Group()
        self.all_projectile2 = pygame.sprite.Group()
        self.image = pygame.image.load('assets/samurai.png')
        self.image = pygame.transform.scale(self.image, (90, 132))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 451
        self.p_return = False
        self.game = game


    def lancer_projectile1(self):
        if self.p_return == False:
            self.all_projectile1.add(Projectile(self, self.game))
        elif self.p_return == True:
            self.all_projectile2.add(Projectile(self, self.game))

    def moove_right(self):
        self.rect.x += self.vitesse

    def moove_left(self):
        self.rect.x -= self.vitesse

    def remove_player(self):
        self.player.remove(self)

