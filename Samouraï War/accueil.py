import pygame

# Images pour notre page d'accueil
class Accueil(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.banner = pygame.image.load('assets/Capture.png')
        self.rect_banner = self.banner.get_rect()
        self.banner = pygame.transform.scale(self.banner, (594, 398))
        self.rect_banner.x = 250
        self.rect_banner.y = 100
        self.all_accueil = pygame.sprite.Group()

class Pause(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image_pause = pygame.image.load('assets/pause.png')
        self.rect_pause = self.image_pause.get_rect()
        self.image_pause = pygame.transform.scale(self.image_pause, (206,206))
        self.rect_pause.x = 437
        self.rect_pause.y = 242
        self.all_pause = pygame.sprite.Group()