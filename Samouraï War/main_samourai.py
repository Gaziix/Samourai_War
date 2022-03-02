import pygame
import random # Module pour l'aléatoire ( pour spawn de momie )
from game import Game
from player import Player

pygame.init()

# Nom, taille et fond d'écran
pygame.display.set_caption("Kinemon | Samouraï War |")

# Icone
icon = pygame.image.load('assets/samurai_head.png')
pygame.display.set_icon(icon)
font = pygame.font.SysFont("monospace", 16)

# Charger le jeu :
game = Game() # On stock notre class pour l'appeler ensuite
player = Player(Game) # On stock notre class pour l'appeler ensuite

# Notre jeu principal
def launch_game():
    while game.running_samourai == True:
        game.background_choice()

        # Affichage des scores et nombres de vagues
        score_display = font.render("Score : " + str(game.score), 1, (255, 255, 0))
        high_score_display = font.render("High Score : " + str(game.high_scored), 1, (255, 255, 0))
        vague_display = font.render("Vague : " + str(game.monster1.wave_number), 1, (255, 255, 0))
        game.screen.blit(score_display, (0, 0))
        game.screen.blit(high_score_display, (0, 15))
        game.screen.blit(vague_display, (980, 0))

        # Déplacement du joueur
        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < game.screen.get_width() and game.moove_right == True:
            game.player.moove_right()
            game.moove_right_life_bar()
            game.player.p_return = False
        elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0 and game.moove_left == True:
            game.player.moove_left()
            game.moove_left_life_bar()
            game.player.p_return = True

        # Orientation du joueur
        game.player_orientation()

        # Gérer la barre de vie du Player
        if game.player.health >= 100 or game.player.health >= 70:
            game.screen.blit(game.life_bar.image1, game.life_bar.rect1)
        elif game.player.health < 70 and game.player.health > 30:
            game.screen.blit(game.life_bar.image2, game.life_bar.rect1)
        elif game.player.health > 0 and game.player.health <= 30:
            game.screen.blit(game.life_bar.image3, game.life_bar.rect1)
        else:
            game.screen.blit(game.life_bar.image4, game.life_bar.rect1)

        # On lance nos projectiles
        game.launch_projectile()
        game.player.all_projectile1.draw(game.screen)  # On affiche nos projectiles qui ont Ã©tÃ© auparavant lancÃ©s
        game.player.all_projectile2.draw(game.screen)

        # On lance tout nos monstres ( si c'est leur vague )
        game.launch_monster()

        # On lance nos cométes
        game.launch_comet()

        # On bouge nos comètes
        game.comet_contact_moove()

        # On les dessine
        game.all_comet.draw(game.screen)

        # On lance les différentes vagues de plus en plus difficiles de momies
        vague = random.randint(1, game.monster1.frequency) # Avec une fréquence qui diminue au fur et à mesure des vaggues
        if vague == 1:
            game.vague()
        pygame.display.flip()   # Actualise la page

        # On prend les actions les gadgets récupérent
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # Pour quitter l'application
                game.running_samourai = False
                game.leave_game()
            elif event.type == pygame.KEYDOWN:  # Une touche enclenchée
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:     # Barre d'espace enclenchée
                    game.projectile_sounds.play()
                    game.player.lancer_projectile1()    # On lance un projectile
                elif event.key == pygame.K_ESCAPE:
                    break_menu()
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

# Notre page d'accueil
def launch_all():
    running_accueil = True
    click_sounds = pygame.mixer.Sound("assets/sounds/click.ogg")
    print("Bienvenue sur Samouraï War !")
    background = pygame.image.load('assets/bg_cacher.png')
    while running_accueil == True:
        font = pygame.font.SysFont("monospace", 16)
        high_score_display = font.render("High Score : " + str(game.high_scored), 1, (255, 255, 0))
        game.screen.blit(background, (0, 0))  # mettre un fond d'écran et viser quelle partie on veut
        game.screen.blit(high_score_display, (0, 0))
        game.screen.blit(game.accueil.banner, game.accueil.rect_banner)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour quitter l'application
                running_accueil = False
                game.remove_accueil()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game.accueil.rect_banner.collidepoint(pos):
                    game.remove_accueil()
                    click_sounds.play()
                    game.reset_game()
                    launch_game()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.remove_accueil()
                    game.reset_game()
                    launch_game()
    pygame.quit() # On quitte la fenêtre pygame
def break_menu():
    running = True
    click_sounds = pygame.mixer.Sound("assets/sounds/click.ogg")
    background = pygame.image.load('assets/bg_cacher.png')
    while running == True:
        game.screen.blit(background, (0, 0))  # mettre un fond d'écran et viser quelle partie on veut
        score_display = font.render("Score : " + str(game.score), 1, (255, 255, 0))
        high_score_display = font.render("High Score : " + str(game.high_scored), 1, (255, 255, 0))
        game.screen.blit(score_display, (0, 0))
        game.screen.blit(high_score_display, (0, 15))
        game.screen.blit(game.pause.image_pause, game.pause.rect_pause)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Pour quitter l'application
                running = False
                game.remove_pause()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if game.pause.rect_pause.collidepoint(pos):
                    game.remove_accueil()
                    click_sounds.play()
                    running = False
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.remove_pause()
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    game.remove_pause()
                    running = False
launch_all()

