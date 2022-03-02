import pygame

class Accueil(pygame.sprite.Sprite):

     def __init__(self):
         super().__init__()
         self.image1 = pygame.image.load('assets/accueil_samourai_war.png')
         self.image2 = pygame.image.load('assets/bg2.jpg') # En attendant le truc de Gatien
         self.image1 = pygame.transform.scale(self.image1, (400, 250))
         self.image2 = pygame.transform.scale(self.image2, (400, 250))
         self.rect1 = self.image1.get_rect()
         self.rect2 = self.image2.get_rect()
         self.rect1.x = 100
         self.rect1.y = 360
         self.rect2.x = 580
         self.rect2.y = 360