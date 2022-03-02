import pygame

# Toutes les classes des monstres / BOSS

# Nos goblins
class Goblin(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.vitesse = 1
        self.health = 20
        self.attack = 5
        self.game = game

        self.image_goblin_1 = pygame.image.load('assets/goblin.png')
        self.image_goblin_1 = pygame.transform.scale(self.image_goblin_1, (118, 128))
        self.rect_golbin_1 = self.image_goblin_1.get_rect()
        self.rect_golbin_1.x = 1080
        self.image_goblin_2 = pygame.image.load('assets/goblin_return.png')
        self.image_goblin_2 = pygame.transform.scale(self.image_goblin_2, (118, 128))
        self.rect_golbin_2 = self.image_goblin_2.get_rect()
        self.rect_golbin_2.x = -100
        self.rect_golbin_2.y = self.rect_golbin_1.y = 460

        self.frequency = 75
        self.vague = 15
        self.wave_number = 1


    def remove_goblin_1(self):
        self.game.all_goblin1.remove(self)

    def remove_goblin_2(self):
        self.game.all_goblin2.remove(self)

    def moove_monster_1(self):
        self.rect_golbin_1.x -= self.vitesse
        if self.rect_golbin_1.x < 0:
            self.remove_goblin_1()
            print("Goblin delete")

    def moove_monster_2(self):
        self.rect_golbin_2.x += self.vitesse
        if self.rect_golbin_2.x > 1080:
            self.remove_goblin_2()
            print("Goblin delete")

    def defend_monster_1(self):
        self.health -= self.game.player.attack
        if self.health == 0:
            self.remove_goblin_1()
            self.game.score += 50
            if self.game.player.health >= 100:
                self.game.player.health = 100
            elif self.game.player.health <= 99:
                self.game.player.health += 20
            print(self.game.player.health)
            print("Le monstre est mort !")

    def defend_monster_2(self):
        self.health -= self.game.player.attack
        if self.health == 0:
            self.remove_goblin_2()
            self.game.score += 50
            if self.game.player.health >= 100:
                self.game.player.health = 100
            elif self.game.player.health <= 99:
                self.game.player.health += 20
            print(self.game.player.health)
            print("Le monstre est mort !")

    def defend_player(self):
        dt = pygame.time.Clock().tick(20)
        if self.game.player.health > 0:
            dt += dt
            if dt >= 0.03:
                self.game.player.health -= self.attack
                print("Le joueur prend des dégats !")
                print(self.game.player.health)
        if self.game.player.health <= 0:
            self.game.player.health = 0


# Notre BOSS ( le colosse )
class Colosse(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.vitesse = 0.5
        self.health = 70
        self.attack = 10
        self.game = game
        self.goblin = Goblin(game)
        self.image_colosse_1 = pygame.image.load('assets/colosse.png')
        self.image_colosse_1 = pygame.transform.scale(self.image_colosse_1, (280, 300))
        self.rect_colosse_1 = self.image_colosse_1.get_rect()
        self.rect_colosse_1.x = 1080
        self.colosse = True

    def remove_colosse(self):
        self.game.all_colosse.remove(self)

    def moove_monster_1(self):
        self.rect_colosse_1.x -= self.vitesse
        if self.rect_colosse_1.x < 0:
            self.remove_colosse()
            print("Ghost delete")

    def defend_monster_1(self):
        self.health -= self.game.player.attack
        if self.health == 0:
            self.remove_colosse()
            self.game.score += 50
            if self.game.player.health >= 100:
                self.game.player.health = 100
            elif self.game.player.health <= 99:
                self.game.player.health += 20
            print(self.game.player.health)
            print("Le monstre est mort !")

    def defend_player(self):
        dt = pygame.time.Clock().tick(20)
        if self.game.player.health > 0:
            dt += dt
            if dt >= 0.03:
                self.game.player.health -= self.attack
                print("Le joueur prend des dégats !")
                print(self.game.player.health)
        if self.game.player.health <= 0:
            self.game.player.health = 0



# Nos fantômes
class Ghost(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.vitesse = 1
        self.health = 30
        self.attack = 5
        self.game = game

        self.image_ghost_1 = pygame.image.load('assets/fantome.png')
        self.image_ghost_1 = pygame.transform.scale(self.image_ghost_1, (120, 100))
        self.rect_ghost_1 = self.image_ghost_1.get_rect()
        self.rect_ghost_1.x = 1080

        self.image_ghost_2 = pygame.image.load('assets/fantome_return.png')
        self.image_ghost_2 = pygame.transform.scale(self.image_ghost_2, (120, 100))
        self.rect_ghost_2 = self.image_ghost_2.get_rect()
        self.rect_ghost_2.x = -100

        self.rect_ghost_1.y = self.rect_ghost_2.y = 570
    def remove_ghost_1(self):
        self.game.all_ghost1.remove(self)

    def remove_ghost_2(self):
        self.game.all_ghost2.remove(self)

    def moove_monster_1(self):
        self.rect_ghost_1.x -= self.vitesse
        if self.rect_ghost_1.x < 0:
            self.remove_ghost_1()
            print("Ghost delete")

    def moove_monster_2(self):
        self.rect_ghost_2.x += self.vitesse
        if self.rect_ghost_2.x > 1080:
            self.remove_ghost_2()
            print("Ghost delete")
    def defend_monster_1(self):
        self.health -= self.game.player.attack
        if self.health == 0:
            self.remove_ghost_1()
            self.game.score += 50
            if self.game.player.health >= 100:
                self.game.player.health = 100
            elif self.game.player.health <= 99:
                self.game.player.health += 20
            print(self.game.player.health)
            print("Le monstre est mort !")

    def defend_monster_2(self):
        self.health -= self.game.player.attack
        if self.health == 0:
            self.remove_ghost_2()
            self.game.score += 50
            if self.game.player.health >= 100:
                self.game.player.health = 100
            elif self.game.player.health <= 99:
                self.game.player.health += 20
            print(self.game.player.health)
            print("Le monstre est mort !")

    def defend_player(self):
        dt = pygame.time.Clock().tick(20)
        if self.game.player.health > 0:
            dt += dt
            if dt >= 0.03:
                self.game.player.health -= self.attack
                print("Le joueur prend des dégats !")
                print(self.game.player.health)
        if self.game.player.health <= 0:
            self.game.player.health = 0

class Mummy(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.vitesse = 1
        self.health = 40
        self.attack = 15
        self.game = game

        self.image_mummy_1 = pygame.image.load('assets/mummy.png')
        self.rect_mummy_1 = self.image_mummy_1.get_rect()
        self.rect_mummy_1.x = 1080

        self.image_mummy_2 = pygame.image.load('assets/mummy_return.png')
        self.rect_mummy_2 = self.image_mummy_2.get_rect()
        self.rect_mummy_2.x = -100

        self.rect_mummy_1.y = self.rect_mummy_2.y = 539

    def remove_mummy_1(self):
        self.game.all_mummy1.remove(self)

    def remove_mummy_2(self):
        self.game.all_mummy2.remove(self)

    def moove_monster_1(self):
        self.rect_mummy_1.x -= self.vitesse
        if self.rect_mummy_1.x < 0:
            self.remove_mummy_1()
            print("Mummy delete")

    def moove_monster_2(self):
        self.rect_mummy_2.x += self.vitesse
        if self.rect_mummy_2.x > 1080:
            self.remove_mummy_2()
            print("Mummy delete")
    def defend_monster_1(self):
        self.health -= self.game.player.attack
        if self.health == 0:
            self.remove_mummy_1()
            self.game.score += 50
            if self.game.player.health >= 100:
                self.game.player.health = 100
            elif self.game.player.health <= 99:
                self.game.player.health += 20
            print(self.game.player.health)
            print("Le monstre est mort !")

    def defend_monster_2(self):
        self.health -= self.game.player.attack
        if self.health == 0:
            self.remove_mummy_2()
            self.game.score += 50
            if self.game.player.health >= 100:
                self.game.player.health = 100
            elif self.game.player.health <= 99:
                self.game.player.health += 20
            print(self.game.player.health)
            print("Le monstre est mort !")

    def defend_player(self):
        dt = pygame.time.Clock().tick(20)
        if self.game.player.health > 0:
            dt += dt
            if dt >= 0.03:
                self.game.player.health -= self.attack
                print("Le joueur prend des dégats !")
                print(self.game.player.health)
        if self.game.player.health <= 0:
            self.game.player.health = 0