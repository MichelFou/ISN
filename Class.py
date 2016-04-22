#Classe du joueur
import pygame
pygame.init()
from random import *
class Player:
        def __init__(self):
                self.level = 1
                self.nextlevelxp = self.level*50
                self.xp = 0
                self.pv = 100
                self.pv_max = 100
                self.attaque = 1
                self.defense = 1
                self.vitesse = 1
                self.magie = 1
                self.degat = 1
                self.discretion = 1
                self.x = 0
                self.y = 0
                self.estmort = False
                self.hasarme = False
                self.hasarmure = None
                self.sort = None
                self.up = pygame.image.load("Hero-up.png")
                self.down = pygame.image.load("Hero-down.png")
                self.left = pygame.image.load("Hero-left.png")
                self.right = pygame.image.load("Hero-right.png")
                self.direction = self.up
                self.image = self.direction
                self.armure = None

        def moveup(self):
                self.direction = self.up
                self.y-=72

        def movedown(self):
                self.direction = self.down
                self.y+=72

        def moveleft(self):
                self.direction = self.left
                self.x-=72
        
        def moveright(self):
                self.direction = self.right
                self.x+=72

        def update(self):
                if self.pv <= 0:
                        self.estmort = True
                        gameover = True
        
        def equiper_armure(self,armure):
                if self.hasarmure:
                        self.old_armure = self.armure
                        self.defense -= self.old_armure.defense
                        self.discretion -= self.old_armure.discretion
                        self.vitesse -= self.old_armure.vitesse
                        self.magie -= self.old_armure.magie
                self.defense += armure.defense
                self.discretion += armure.discretion
                self.vitesse += armure.vitesse
                self.magie += armure.magie
                self.armure = armure
                self.hasarmure = True
        
        def equiper_arme(self,arme_name):
                if self.hasarme:
                        self.attaque -= old_arme_name.attaque
                        self.vitesse -= old_arme_name.vitesse
                        self.degat -= old_arme_name.degat
                        self.magie -= old_arme_name.magie
                self.attaque += arme_name.attaque
                self.vitesse += arme_name.vitesse
                self.degat += arme_name.degat
                self.magie += arme_name.magie
                old_arme_name = arme_name
                self.hasarme = True

        def blesse(self,mob_name):
                if randint(1,30)<mob_name.attaque:
                        if randint(1,30)>self.vitesse:
                                valeur = randint(1,mob_name.degat)-randint(1,self.defense)
                                if valeur > 0:
                                        self.pv -= valeur
                                else:
                                        self.pv -= 0
                        else:
                                esquive = True
                                print "Esquive !"
                else:
                        echec = True
                        print "Echec !"
                

class Armure:
        def __init__(self):
                self.discretion = 0
                self.defense = 0
                self.vitesse = 0
                self.magie = 0
        class Plastrondecuivre:
                def __init__(self):
                        self.discretion = -1
                        self.defense = 3
                        self.vitesse = -1
                        self.magie = 0
        class Capedinvisibilite:
                def __init__(self):
                        self.discretion = 2
                        self.vitesse = 2
                        self.defense = 0
                        self.magie = 0
        class Manteaudevoleur:
                def __init__(self):
                        self.discretion = 1
                        self.defense = -1
                        self.vitesse = 2
                        self.magie = 0
        class Armuredeplaques:
                def __init__(self):
                        self.discretion = -2
                        self.defense = 4
                        self.vitesse = -2
                        self.magie = 0
        class Robedemage:
                def __init__(self):
                        self.discretion = 0
                        self.defense = -2
                        self.vitesse = 1
                        self.magie = 3

class Arme:
        def __init__(self):
                self.attaque = 0
                self.vitesse = 0
                self.degat = 0
                self.magie = 0
        class Epee:
                def __init__(self):
                        self.attaque = 2
                        self.vitesse = -1
                        self.degat = 2
                        self.magie = 0
        class Masselourde:
                def __init__(self):
                        self.attaque = -2
                        self.vitesse = -2
                        self.degat = 4
                        self.magie = 0
        class Dague:
                def __init__(self):
                        self.attaque = 1
                        self.vitesse = 2
                        self.degat = 0
                        self.magie = 0
        class Baton:
                def __init__(self):
                        self.attaque = 0
                        self.vitesse = 0
                        self.degat = -1
                        self.magie = 3
        class Hache:
                def __init__(self):
                        self.attaque = -1
                        self.vitesse = -1
                        self.degat = 2
                        self.magie = 0
        class Masseapiques:
                def __init__(self):
                        self.attaque = -1
                        self.vitesse = -1
                        self.degat = 3
                        self.magie = 0

class Mobs:
        def __init__(self):
                self.pv = 0
                self.vitesse = 0
                self.degat = 0
                self.attaque = 0
                self.defense = 0
                self.perception = 0
                self.xp = 0
        class Loup:
                def __init__(self):
                        self.image = pygame.image.load("loup.png").convert_alpha()
                        self.pv = 20
                        self.vitesse = 17
                        self.attaque = 10
                        self.degat = 5
                        self.defense = 7
                        self.perception = 20
                        self.xp = 7
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp

        class Orc:
                def __init__(self):
                        self.image = pygame.image.load("orc.png").convert_alpha()
                        self.pv = 20
                        self.vitesse = 15
                        self.attaque = 15
                        self.degat = 8
                        self.defense = 8
                        self.perception = 20
                        self.xp = 8
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp
        class Gobelin:
                def __init__(self):
                        self.image = pygame.image.load("gobelin.png").convert_alpha()
                        self.pv = 20
                        self.vitesse = 15
                        self.attaque = 18
                        self.degat = 7
                        self.defense = 8
                        self.perception = 10
                        self.xp = 8
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp
        class Centaure:
                def __init__(self):
                        self.image = pygame.image.load("centaure.png").convert_alpha()
                        self.pv = 25
                        self.vitesse = 20
                        self.attaque = 20
                        self.degat = 8
                        self.defense = 10
                        self.perception = 17
                        self.xp = 9
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp
        class Cavalier:
                def __init__(self):
                        self.image = pygame.image.load("cavalier.png").convert_alpha()
                        self.pv = 25
                        self.vitesse = 20
                        self.attaque = 21
                        self.degat = 9
                        self.defense = 15
                        self.perception = 20
                        self.xp = 12
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp
        class Mort_vivant:
                def __init__(self):
                        self.image = pygame.image.load("mort_vivant.png").convert_alpha()
                        self.pv = 15
                        self.vitesse = 10
                        self.attaque = 8
                        self.degat = 5
                        self.defense = 8
                        self.perception = 10
                        self.xp = 7
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp
        class Squelette:
                def __init__(self):
                        self.image = pygame.image.load("squelette.png").convert_alpha()
                        self.pv = 15
                        self.vitesse = 13
                        self.attaque = 10
                        self.degat = 6
                        self.defense = 6
                        self.perception = 15
                        self.xp = 8
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp
        class Araignee:
                def __init__(self):
                        self.image = pygame.image.load("araignee.png").convert_alpha()
                        self.pv = 20
                        self.vitesse = 17
                        self.attaque = 23
                        self.degat = 8
                        self.defense = 10
                        self.perception = 17
                        self.xp = 10
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp
        class Persephon:
                def __init__(self):
                        self.image = pygame.image.load("persephon.png").convert_alpha()
                        self.pv = 70
                        self.vitesse = 17
                        self.attaque = 21
                        self.degat = 25
                        self.defense = 15
                        self.perception = 30
                        self.xp = 50
                def update(self):
                        if self.pv <= 0:
                                self.estmort = True
                                player.xp += self.xp
                                
                def attack(self,player_name):
                        player_name.blesse(self)
