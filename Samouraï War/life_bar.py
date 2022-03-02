import pygame

# Nos barres de vie : Player et Monster
class Life_Bar(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image1 = pygame.image.load('assets/life_bar/full_life.png')
        self.image2 = pygame.image.load('assets/life_bar/middle_life.png')
        self.image3 = pygame.image.load('assets/life_bar/critic_life.png')
        self.image4 = pygame.image.load('assets/life_bar/no_life.png')

        self.image1 = pygame.transform.scale(self.image1, (100, 50))
        self.image2 = pygame.transform.scale(self.image2, (100, 50))
        self.image3 = pygame.transform.scale(self.image3, (100, 50))
        self.image4 = pygame.transform.scale(self.image4, (100, 50))

        self.rect1 = self.image1.get_rect()
