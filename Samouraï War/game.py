import pygame
from random import randint
from player import Player
from monster import Ghost, Goblin, Colosse, Mummy
from life_bar import Life_Bar
from accueil import Accueil, Pause
from fire_ball import Fire_Ball
from projectile import Projectile

# Notre jeu
class Game:

    def __init__(self):
        self.pressed = {}
        self.player = Player(Game)
        self.monster1 = Goblin(Game)
        self.monster2 = Colosse(Game)
        self.monster3 = Ghost(Game)
        self.monster4 = Mummy(Game)
        self.all_goblin1 = pygame.sprite.Group()
        self.all_goblin2 = pygame.sprite.Group()
        self.all_mummy1 = pygame.sprite.Group()
        self.all_mummy2 = pygame.sprite.Group()
        self.all_ghost1 = pygame.sprite.Group()
        self.all_ghost2 = pygame.sprite.Group()
        self.all_colosse = pygame.sprite.Group()
        self.life_bar = Life_Bar(Game)
        self.accueil = Accueil(Game)
        self.pause = Pause(Game)
        self.score = 0
        self.projectile = Projectile(self.player, self)
        self.high_scored = 0
        self.comet = Fire_Ball(Game)
        self.all_comet = pygame.sprite.Group()
        self.comet_storm = False
        self.vague_test = 0 # Compteur de monstre/vague
        self.screen = pygame.display.set_mode((1080, 691))
        self.background = pygame.image.load('assets/bg.png') # Nos fonds d'écran des différentes vagues
        self.background2 = pygame.image.load('assets/maudit.jpg')
        self.background3 = pygame.image.load('assets/bg.jpg')
        self.game_over_sounds = pygame.mixer.Sound("assets/sounds/game_over.ogg")
        self.comet_sounds = pygame.mixer.Sound("assets/sounds/meteorite.ogg")
        self.projectile_sounds = pygame.mixer.Sound("assets/sounds/tir.ogg")
        self.running_samourai = True
        self.moove_right = True
        self.moove_left = True

    def moove_right_life_bar(self):
        self.life_bar.rect1.x += self.player.vitesse

    def moove_left_life_bar(self):
        self.life_bar.rect1.x -= self.player.vitesse

    def remove_accueil(self):
        self.accueil.all_accueil.remove(self)

    def remove_pause(self):
        self.pause.all_pause.remove(self)

    def high_score(self):
        if self.score > self.high_scored:
            self.high_scored = self.score

    def launcher_comet(self):
        self.all_comet.add(Fire_Ball(self))

    def launch_comet(self):
        # On lance nos cométes
        if self.comet_storm == True and self.comet.comet_test <= self.comet.comet_number:
            comete = randint(1, self.comet.frequency)
            if comete == 1:
                self.launcher_comet()
                self.comet_sounds.play()
                self.comet.comet_test += 1
            if self.comet_storm == True and self.comet.comet_test > self.comet.comet_number:
                self.comet.comet_test = 0
                self.comet_storm = False
                self.score += 500
                self.comet.comet_number += 10
                self.comet.frequency -= 5
                self.monster1.wave_number += 1

    def comet_contact_moove(self):
        for comet in self.all_comet:
            comet.moove_comet()
            if comet.rect.colliderect(self.player.rect):
                comet.player_contact()
                if self.player.health <= 0:
                    print("Les comètes ont tué le Player")
                    print("La partie est terminée")
                    self.leave_game()
                    self.running_samourai = False
                    self.game_over_sounds.play()

    def vague(self):
        # Les vagues qui déroulent automatiquement
        if self.monster1.wave_number < 6: # Pour accélèrer le nbre de spawn
            retard = randint(1, 2)
        else:
            retard = 1
        if self.comet_storm == False and self.vague_test < self.monster1.vague and retard == 1:
            right_or_left = randint(1, 2)
            if right_or_left == 1: # On choisis à droite
                if self.monster1.wave_number < 3: # On choisit le monstre en fonction du niveau de jeu actuel
                    self.all_goblin1.add(Goblin(self)) # Launcher de mummy venant de droite
                elif self.monster1.wave_number >= 3 and self.monster1.wave_number < 6:
                    self.all_ghost1.add(Ghost(self))
                elif self.monster1.wave_number >= 6:
                    self.all_mummy1.add(Mummy(self))
            else: # On choisit à gauche
                if self.monster1.wave_number < 3: # Suivant le niveau, on affiche différent monstre
                    self.all_goblin2.add(Goblin(self))  # Launcher de mummy venant de droite
                elif self.monster1.wave_number >= 3 and self.monster1.wave_number < 6:
                    self.all_ghost2.add(Ghost(self))
                elif self.monster1.wave_number >= 6:
                    self.all_mummy2.add(Mummy(self))
            if self.monster1.wave_number > 1 and self.monster2.colosse == True:
                self.all_colosse.add(Colosse(self))
                self.monster2.colosse = False
            self.vague_test += 1
            print("La {0}ème escadrille t'envoie une momie !".format(self.monster1.wave_number))
            if self.vague_test == self.monster1.vague:
                self.vague_test = 0
                self.comet_storm = True
                self.monster1.vague = 6 * self.monster1.wave_number
                self.monster1.frequency -= 5
                self.monster2.colosse = True
                print("La {0}ème a été anéantie !".format(self.monster1.wave_number))

    def leave_game(self):
        # On supprime tout pour ne pas surcharger
        self.player.remove_player()
        for goblin in self.all_goblin1:
            goblin.remove_goblin_1()
        for goblin in self.all_goblin2:
            goblin.remove_goblin_2()
        for ghost in self.all_ghost1:
            ghost.remove_ghost_1()
        for ghost in self.all_ghost2:
            ghost.remove_ghost_2()
        for mummy in self.all_mummy1:
            mummy.remove_mummy_1()
        for mummy in self.all_mummy2:
            mummy.remove_mummy_2()
        for colosse in self.all_colosse:
            colosse.remove_colosse()
        self.all_colosse.remove()
        self.life_bar.remove()
        for projectile in self.player.all_projectile1:
            projectile.remove_projectile_1()
        for projectile in self.player.all_projectile2:
            projectile.remove_projectile_2()
        self.high_score()
        for comet in self.all_comet:
            comet.remove_comet()

    def reset_game(self):
        # On remet toute nos constantes à 0
        self.player.health = self.player.max_health
        self.player.rect.x = 400
        self.player.rect.y = 451
        self.life_bar.rect1.x = 400
        self.life_bar.rect1.y = 420
        self.score = 0
        self.comet_storm = False
        self.monster2.colosse = True
        self.comet.comet_test = 0
        self.comet.frequency = 45
        self.comet.comet_number = 20
        self.vague_test = 0
        self.monster1.frequency = 75
        self.monster1.vague = 10
        self.monster1.wave_number = 1
        self.running_samourai = True

    def launch_projectile(self):
        # On lance les projectiles
        for projectile in self.player.all_projectile1:
            projectile.move1()
        for projectile in self.player.all_projectile2:
            projectile.move2()

    def background_choice(self):
        # On choisis en fonction de la vague le background
        if self.monster1.wave_number < 3:
            self.screen.blit(self.background, (0, 0))  # Fond d'écran
        elif self.monster1.wave_number >= 3 and self.monster1.wave_number < 6:
            self.screen.blit(self.background2, (0, -280))  # Fond d'écran
            self.player.rect.y = 555
            self.life_bar.rect1.y = 519
        elif self.monster1.wave_number >= 6:
            self.screen.blit(self.background3, (0, -200))  # Fond d'écran
            self.player.rect.y = 530
            self.life_bar.rect1.y = 499

    def player_orientation(self):
        # Sens du joueur ( orientation droite/gauche )
        if self.player.p_return == False:
            self.screen.blit(self.player.image, self.player.rect)
        elif self.player.p_return == True:
            player_image_return = pygame.image.load('assets/samurai.png')
            player_image_return = pygame.transform.scale(player_image_return, (90, 132))
            self.screen.blit(player_image_return, self.player.rect)

    def launch_monster(self):
        for colosse in self.all_colosse:
            if self.monster1.wave_number < 3:
                colosse.rect_colosse_1.y = 290
            elif self.monster1.wave_number >= 3 and self.monster1.wave_number < 6:
                colosse.rect_colosse_1.y = 400
            else:
                colosse.rect_colosse_1.y = 380
            self.screen.blit(colosse.image_colosse_1, colosse.rect_colosse_1)
            colosse.moove_monster_1()
            for projectile in self.player.all_projectile1:  # Contact projectile/momie
                if colosse.rect_colosse_1.colliderect(projectile.rect):
                    projectile.remove_projectile_1()
                    print("Boule de feu dans ta gueule !")
                    colosse.defend_monster_1()
            if colosse.rect_colosse_1.colliderect(self.player.rect):  # Collision entre momie et Player
                colosse.vitesse = 0
                colosse.defend_player()
                self.moove_right = False
                if self.player.health <= 0:  # Si le joueur n'a pas de vie alors la partie est terminée
                    print("Le Player n'est plus des notre ! RIP")
                    print("Retour à  la page d'accueil")
                    self.leave_game()
                    self.running_samourai = False
                    self.game_over_sounds.play()
            elif colosse.rect_colosse_1.x > self.player.rect.x:
                colosse.vitesse = 1
                self.moove_right = True

        # Goblin contact + déplacement ( goblin venant de droite ):
        for goblin in self.all_goblin1:
            self.screen.blit(goblin.image_goblin_1, goblin.rect_golbin_1)
            goblin.moove_monster_1()
            for projectile in self.player.all_projectile1:  # Contact projectile/momie
                if goblin.rect_golbin_1.colliderect(projectile.rect):
                    projectile.remove_projectile_1()
                    print("Boule de feu dans ta gueule !")
                    goblin.defend_monster_1()
            if goblin.rect_golbin_1.colliderect(self.player.rect):  # Collision entre momie et Player
                goblin.vitesse = 0
                goblin.defend_player()
                self.moove_right = False
                if self.player.health <= 0:  # Si le joueur n'a pas de vie alors la partie est terminÃ©e
                    print("Le Player n'est plus des notre ! RIP")
                    print("Retour à  la page d'accueil")
                    self.leave_game()
                    self.running_samourai = False
                    self.game_over_sounds.play()
            elif goblin.rect_golbin_1.x > self.player.rect.x:
                goblin.vitesse = 1
                self.moove_right = True

        # Goblin venant de gauche
        for goblin in self.all_goblin2:
            self.screen.blit(goblin.image_goblin_2, goblin.rect_golbin_2)
            goblin.moove_monster_2()
            for projectile in self.player.all_projectile2:
                if goblin.rect_golbin_2.colliderect(projectile.rect):
                    projectile.remove_projectile_2()
                    print("Boule de feu dans ta gueule !")
                    goblin.defend_monster_2()
            if goblin.rect_golbin_2.colliderect(self.player.rect):  # Collision entre momie et Player
                goblin.vitesse = 0
                goblin.defend_player()
                self.moove_left = False
                if self.player.health <= 0:  # Si le joueur n'a pas de vie alors la partie est terminée
                    print("Le Player n'est plus des notre ! RIP")
                    print("Retour à  la page d'accueil")
                    self.leave_game()
                    self.running_samourai = False
                    self.game_over_sounds.play()
            elif goblin.rect_golbin_2.x < self.player.rect.x:
                goblin.vitesse = 1
                self.moove_left = True

        # Ghost venant de droite
        for ghost in self.all_ghost1:
            self.screen.blit(ghost.image_ghost_1, ghost.rect_ghost_1)
            ghost.moove_monster_1()
            for projectile in self.player.all_projectile1:  # Contact projectile/momie
                if ghost.rect_ghost_1.colliderect(projectile.rect):
                    projectile.remove_projectile_1()
                    print("Boule de feu dans ta gueule !")
                    ghost.defend_monster_1()
            if ghost.rect_ghost_1.colliderect(self.player.rect):  # Collision entre momie et Player
                ghost.vitesse = 0
                ghost.defend_player()
                self.moove_right = False
                if self.player.health <= 0:  # Si le joueur n'a pas de vie alors la partie est terminée
                    print("Le Player n'est plus des notre ! RIP")
                    print("Retour à  la page d'accueil")
                    self.leave_game()
                    self.running_samourai = False
                    self.game_over_sounds.play()
            elif ghost.rect_ghost_1.x > self.player.rect.x:
                ghost.vitesse = 1
                self.moove_right = True

        for ghost in self.all_ghost2:
            self.screen.blit(ghost.image_ghost_2, ghost.rect_ghost_2)
            ghost.moove_monster_2()
            for projectile in self.player.all_projectile2:  # Contact projectile/momie
                if ghost.rect_ghost_2.colliderect(projectile.rect):
                    projectile.remove_projectile_2()
                    print("Boule de feu dans ta gueule !")
                    ghost.defend_monster_2()
            if ghost.rect_ghost_2.colliderect(self.player.rect):  # Collision entre momie et Player
                ghost.vitesse = 0
                ghost.defend_player()
                self.moove_left = False
                if self.player.health <= 0:  # Si le joueur n'a pas de vie alors la partie est terminée
                    print("Le Player n'est plus des notre ! RIP")
                    print("Retour à  la page d'accueil")
                    self.leave_game()
                    self.running_samourai = False
                    self.game_over_sounds.play()
            elif ghost.rect_ghost_2.x < self.player.rect.x:
                ghost.vitesse = 1
                self.moove_left = True

        # Mummy venant de droite
        for mummy in self.all_mummy1:
            self.screen.blit(mummy.image_mummy_1, mummy.rect_mummy_1)
            mummy.moove_monster_1()
            for projectile in self.player.all_projectile1:  # Contact projectile/momie
                if mummy.rect_mummy_1.colliderect(projectile.rect):
                    projectile.remove_projectile_1()
                    print("Boule de feu dans ta gueule !")
                    mummy.defend_monster_1()
            if mummy.rect_mummy_1.colliderect(self.player.rect):  # Collision entre momie et Player
                mummy.vitesse = 0
                mummy.defend_player()
                self.moove_right = False
                if self.player.health <= 0:  # Si le joueur n'a pas de vie alors la partie est terminée
                    print("Le Player n'est plus des notre ! RIP")
                    print("Retour à  la page d'accueil")
                    self.leave_game()
                    self.running_samourai = False
                    self.game_over_sounds.play()
            elif mummy.rect_mummy_1.x > self.player.rect.x:
                mummy.vitesse = 1
                self.moove_right = True

        # Mummy venant de gauche
        for mummy in self.all_mummy2:
            self.screen.blit(mummy.image_mummy_2, mummy.rect_mummy_2)
            mummy.moove_monster_2()
            for projectile in self.player.all_projectile2:  # Contact projectile/momie
                if mummy.rect_mummy_2.colliderect(projectile.rect):
                    projectile.remove_projectile_2()
                    print("Boule de feu dans ta gueule !")
                    mummy.defend_monster_2()
            if mummy.rect_mummy_2.colliderect(self.player.rect):  # Collision entre momie et Player
                mummy.vitesse = 0
                mummy.defend_player()
                self.moove_left = False
                if self.player.health <= 0:  # Si le joueur n'a pas de vie alors la partie est terminée
                    print("Le Player n'est plus des notre ! RIP")
                    print("Retour à  la page d'accueil")
                    self.leave_game()
                    self.running_samourai = False
                    self.game_over_sounds.play()
            elif mummy.rect_mummy_2.x < self.player.rect.x:
                mummy.vitesse = 1
                self.moove_left = True