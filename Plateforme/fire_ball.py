import pygame
import random

# Class de notre pluie de boule de feu
class Fire_Ball(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.vitesse = 3
        self.attack = 10
        self.game = game
        self.image = pygame.image.load('assets_samourai/comet1.png')
        self.image = pygame.transform.scale(self.image, (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000)
        self.rect.y = -140
        self.comet_test = 0
        self.comet_number = 20
        self.frequency = 45

    def remove_comet(self):
        self.game.all_comet.remove(self)

    def moove_comet(self):
        self.rect.y += self.vitesse
        if self.game.monster1.wave_number < 3:
            if self.rect.y > 500:
                self.remove_comet() # Lorsqu'il atteint le sol, il se delete
        elif self.game.monster1.wave_number >= 3 and self.game.monster1.wave_number < 6:
            if self.rect.y > 595:
                self.remove_comet()
        elif self.game.monster1.wave_number >= 6:
            if self.rect.y > 570:
                self.remove_comet()

    def player_contact(self):
        self.game.player.health -= self.attack
        self.game.life_bar.rect_form[2] -= self.attack
        self.remove_comet()
        print(self.game.player.health)
        print("Comètes dans la tronche !")

