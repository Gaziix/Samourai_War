import pygame

# Nos barres de vie : Player et Monster
class Life_Bar(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.color = (0, 200, 0)  # Code couleur RGB du vert
        self.rect_start = 400
        self.rect_end = 100
        self.rect_form = pygame.Rect(395, 440, 100, 5)