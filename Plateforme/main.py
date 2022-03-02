from pygame.locals import *
from accueil_platform import Accueil
from main_samourai import *

pygame.init()
pygame.font.init()

# On stock nos instances dans des variables
accueil = Accueil()

screen = pygame.display.set_mode((1080, 691))
pygame.display.set_icon(pygame.image.load('assets/logo.ico'))

font_enter = pygame.font.SysFont('Trebuchet MS', 50)
font1 = pygame.font.Font('assets/Candy Beans.otf', 100)  # create a new Font object from a file
font2 = pygame.font.SysFont('Trebuchet MS', 20)
font3 = pygame.font.Font(None, 80)  # create a new Font object from a file
font4 = pygame.font.Font(None, 120)
font5 = pygame.font.Font('assets/varsity_regular.ttf', 50)
background1 = pygame.image.load('assets/bg4.jpg')
background1 = pygame.transform.scale(background1, (1280, 720))

# Nos ustensiles
def get_pseudo():
    txt = ""
    pygame.display.set_caption("Kinemon | Pseudo |")
    title = font4.render("Entrez votre pseudo", True, (255, 255, 255))
    x, y, z = 255, 0, 0
    running = True
    while running:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():   # Tout lettre ou truc affichable quoi tapé au clavier
                    txt += str(evt.unicode)     # chaine encodé en ascii, comme l'ordi
                    # print txt
                elif evt.key == K_BACKSPACE:    # On supprime
                    txt = txt[:-1]  # On vise le dernier de la liste ascii
                elif evt.key == K_RETURN:   # On fini de rentrer le pseudo
                    if txt == "":
                        pass
                    else:
                        return txt
            elif evt.type == QUIT:
                running = False
        screen.blit(background1, (0, 0))
        if x > 200:
            z = 0
            y += 1
        if y > 200:
            x = 0
            z += 1
        if z > 200:
            y = 0
            x += 1
        block = font3.render(txt, True, (x, y, z))  # On affiche txt, avec antialias et en blanc ( mode rgb )
        rect = block.get_rect() # On récupère les coordonnées de notre rectangle
        # On ajuste au centre, rect.center permet de centrer horizontalement, plus il y a de txt, et c'est tjrs centré
        # screen.get_rect().center --> On ajuste verticalement + on réduit les bugs
        rect.center = screen.get_rect().center
        screen.blit(title, (120, 200))
        screen.blit(block, rect) # On blit
        pygame.display.flip() # On répète la boucle
    pygame.font.quit()
    pygame.quit()


def accueil_platform():
    running = True
    pygame.display.set_caption("Kinemon | Platform |")

    welcome_1 = font1.render("Welcome {0}".format(pseudo), True, (0, 0, 0))
    welcome_2 = font1.render("on KINEMON", True, (0, 0, 0))
    welcome_3 = font2.render("Session : {0}".format(pseudo), True, (0, 0, 0))
    rect1 = welcome_1.get_rect()
    rect1.center = screen.get_rect().center
    rect1.y -= 100
    x = 255
    n = True
    while running == True:
        pygame.display.set_caption("Kinemon | Platform |")
        screen.blit(background1, (0, 0))  # mettre un fond d'écran et viser quelle partie on veut
        screen.blit(welcome_1, rect1)
        screen.blit(welcome_2, (300, 300))
        screen.blit(welcome_3, (0, 0))
        if x < 255 and n == True:
            x += 5
            n = True
        else:
            n = False
            x -= 5
            if n == False and x == 0:
                n = True
        enter = font_enter.render("--- Press ENTER ---", True, (x, x, x))
        rect2 = enter.get_rect()
        rect2.center = screen.get_rect().center
        rect2.y += 100
        screen.blit(enter, rect2)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour quitter l'application
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    platform()
    pygame.font.quit()
    pygame.quit()

def platform():
    running = True
    samurai = font5.render("SAMOURAÏ WAR", True, (0, 0, 0))
    ninja = font5.render("NINJA ESCAPE", True, (0, 0, 0))
    welcome_3 = font2.render("Session : {0}".format(pseudo), True, (0, 0, 0))
    logo_jeu = pygame.image.load('assets/logo_jeu.png')
    rect = background1.get_rect()
    while running == True:
        pygame.display.set_caption("Kinemon | Platform |")
        # high_score_display = font.render("High Score : " + str(game.high_scored), 1, (255, 255, 0))
        screen.blit(background1, (0, 0))  # mettre un fond d'écran et viser quelle partie on veut
        screen.blit(logo_jeu, (380, 130))
        screen.blit(accueil.image1, accueil.rect1)
        screen.blit(accueil.image2, accueil.rect2)
        screen.blit(welcome_3, (0, 0))
        screen.blit(samurai, (110, 310))
        screen.blit(ninja, (610, 310))
        # screen.blit(high_score_display, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour quitter l'application
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if accueil.rect1.collidepoint(pos):
                    launch_all()
                elif accueil.rect2.collidepoint(pos):
                    pass # Go ninja escape
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

# Menu d'exécution :
pseudo = get_pseudo()
if pseudo != None:
    accueil_platform()