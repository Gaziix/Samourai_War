import pygame
from pygame.locals import *


def name():
    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    txt = ""
    font = pygame.font.Font(None, 100) # create a new Font object from a file
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha(): # Tout lettre ou truc affichable quoi tapé au clavier
                    txt += str(evt.unicode) # chaine encodé en ascii, comme l'ordi
                    # print txt
                elif evt.key == K_BACKSPACE: # On supprime
                    txt = txt[:-1] # On vise le dernier de la liste ascii
                elif evt.key == K_SPACE: # Un espace est compté comme un espace
                    txt += " "
                elif evt.key == K_RETURN: # On fini de rentrer le pseudo
                    return txt
            elif evt.type == QUIT:
                return txt
        screen.fill((0, 0, 0)) # On rempli le bg de noir sans donné de propriété spécifique
        block = font.render(txt, True, (255, 255, 255)) # On affiche txt, avec antialias et en blanc ( mod rgb )
        rect = block.get_rect() # On récupère les coordonnées de notre rectangle
        # On les ajuste au centre, rect.center permet de centrer horizontalement, même plus il y a de txt, et c'est tjrs centré
        # screen.get_rect().center --> On ajuste verticalement + on réduit les bugs
        rect.center = screen.get_rect().center
        screen.blit(block, rect) # On blit
        pygame.display.flip() # On répète la boucle


pseudo = name()
print(pseudo)