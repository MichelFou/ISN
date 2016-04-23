#Classe du joueur
import pygame
pygame.init()
from random import *
from pygame.locals import*
from bibliotheque import *
#from Menu import *
from actions import *

fenetre = pygame.display.set_mode((1024,768))

class Player:
        def __init__(self):
                self.level = 1
                self.nextlevelxp = self.level*50
                self.xp = 0
                self.pv = 100
                self.pvmax = 100
                self.attaque = 1
                self.defense = 1
                self.vitesse = 1
                self.magie = 1
                self.degat = 1
                self.discretion = 1
                self.x = 30
                self.y = 47
                self.estmort = False
                self.hasarme = False
                self.hasarmure = None
                self.sort = None
                self.armure = None
                self.up = pygame.image.load("Images/Hero-up.png")
                self.down = pygame.image.load("Images/Hero-down.png")
                self.left = pygame.image.load("Images/Hero-left.png")
                self.right = pygame.image.load("Images/Hero-right.png")
                self.direction = self.up
                self.image = self.direction                
                
        def moveup(self):
                self.direction = self.up
                self.y-=1

        def movedown(self):
                self.direction = self.down
                self.y+=1

        def moveleft(self):
                self.direction = self.left
                self.x-=1
        
        def moveright(self):
                self.direction = self.right
                self.x+=1

        def update(self):
                if self.pv <= 0:
                        self.estmort = True
                        gameover = True
                fenetre.blit(self.image,(self.x,self.y))
                if self.xp == nextlevelxp:
                        self.xp = 0
                        levelup = True
                if self.xp > nextlevelxp:
                        self.xp -= self.nextlevelxp
                        levelup = True
                if levelup:
                        self.levelup()
                        
        def levelup(self):
                self.pv += 5
                self.pv_max += 5
                self.attaque += 1
                self.defense += 1
                self.vitesse += 1
                self.magie += 1
                self.degat += 1
                self.discretion += 1
        
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
                                print ("Coup !")
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
        def attack(self,mob_name):
                mob_name.blesse()

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
                self.x = 0
                self.y = 0
        class Loup:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/wolf.png").convert_alpha()
                        self.pv = 20
                        self.vitesse = 17
                        self.attaque = 10
                        self.degat = 5
                        self.defense = 7
                        self.perception = 20
                        self.xp = 7
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                        
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
                def blesse(self):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
                def attack(self):
                        player.blesse(self)
                        

        class Orc:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/orc.png").convert_alpha()
                        self.pv = 20
                        self.vitesse = 15
                        self.attaque = 15
                        self.degat = 8
                        self.defense = 8
                        self.perception = 20
                        self.xp = 8
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                        
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
                def blesse(self):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
                def attack(self):
                        player.blesse(self)
                def blesse(self,player):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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

        class Gobelin:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/gobelin.png").convert_alpha()
                        self.pv = 20
                        self.vitesse = 15
                        self.attaque = 18
                        self.degat = 7
                        self.defense = 8
                        self.perception = 10
                        self.xp = 8
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
                        
                def blesse(self,player):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
        class Centaure:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/centaurus.png").convert_alpha()
                        self.pv = 25
                        self.vitesse = 20
                        self.attaque = 20
                        self.degat = 8
                        self.defense = 10
                        self.perception = 17
                        self.xp = 9
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                        
                def blesse(self,player):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
        class Mort_vivant:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/undead.png").convert_alpha()
                        self.pv = 15
                        self.vitesse = 10
                        self.attaque = 8
                        self.degat = 5
                        self.defense = 8
                        self.perception = 10
                        self.xp = 7
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                        
                def blesse(self,player):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
        class Squelette:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/skeleton.png").convert_alpha()
                        self.pv = 15
                        self.vitesse = 13
                        self.attaque = 10
                        self.degat = 6
                        self.defense = 6
                        self.perception = 15
                        self.xp = 8
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                        
                def blesse(self,player):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
        class Araignee:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/spider.png").convert_alpha()
                        self.pv = 20
                        self.vitesse = 17
                        self.attaque = 23
                        self.degat = 8
                        self.defense = 10
                        self.perception = 17
                        self.xp = 10
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                        
                def blesse(self,player):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
        class Persephon:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/persephon.png").convert_alpha()
                        self.pv = 70
                        self.vitesse = 17
                        self.attaque = 21
                        self.degat = 25
                        self.defense = 15
                        self.perception = 30
                        self.xp = 50
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
                                
                def attack(self,player):
                        player.blesse(self)
        
                def blesse(self,player):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
        class Cavalier:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
                        self.image = pygame.image.load("Images/knight.png").convert_alpha()
                        self.pv = 25
                        self.vitesse = 20
                        self.attaque = 21
                        self.degat = 9
                        self.defense = 15
                        self.perception = 20
                        self.xp = 12
                def update(self):
                        if self.pv <= 0:
                                player.xp += self.xp
                                del(self)
                        if player.x == self.x or player.y == self.y:
                                if player.y - 1 == self.y:
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 == self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 == self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 == self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y == self.y or Mobs.x == self.x:
                                                if Mobs.y - 1 == self.y or Mobs.y + 1 == self.y or Mobs.x - 1 == self.x or Mobs.x + 1 == self.x:
                                                        self.attack(Mobs)
                                                        self.move = False
                                                else:
                                                        self.move = True
                                        else:
                                                self.move = True
                                if self.move:
                                        if randint(1,self.perception) > player.discretion:
                                                self.diffx = abs(self.x - player.x)
                                                self.diffy = abs(self.y - player.y)
                                                if self.diffx > self.diffy:
                                                        if self.x > player.x:
                                                                self.moveleft()
                                                        if self.x < player.x:
                                                                self.moveright()
                                                if self.diffx < self.diffy:
                                                        if self.y > player.y:
                                                                self.moveup()
                                                        if self.y < player.y:
                                                                self.movedown()
                        fenetre.blit(self.image,(self.x,self.y))
                def moveleft(self):
                        if structure_niveau[self.y][self.x-1]=='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]=='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]=='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]=='h':
                                self.x += 1
                                
                def attack(self,player):
                        player.blesse(self)
        
                def blesse(self,player):
                        if randint(1,30)<player.attaque:
                                if randint(1,30)>self.vitesse:
                                        valeur = randint(1,player.degat)-randint(1,self.defense)
                                        print "Coup !"
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
                
class Spell:
        def __init__(self):
                self.duree = 0
                self.attaque = 0
                self.vitesse = 0
                self.recharge = 0
                self.degat = 0
                self.actif = 0
                self.dispo = 0
                self.tempsecoule = 0
        class Berserk:
                def __init__(self):
                        self.duree = 7 + player.magie
                        self.recharge = 20 - player.magie
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if self.actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge >= self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                        if self.tempsecoule >= self.duree:
                                player.attaque -= 2
                                player.vitesse -= 2
                                player.degat -= 1
                                self.actif = 0
                                self.tempsrecharge += 1
                def lancer(self):
                        if self.dispo:
                                player.attaque +=2
                                player.vitesse += 2
                                player.degat += 1
                                self.dispo = 0
                                self.actif = 1
        class Corps_Dacier:
                def __init__(self):
                        self.duree = 7 + player.magie
                        self.recharge = 30 - player.magie
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge >= self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                        if self.tempsecoule >= self.duree:
                                player.defense -= 4
                                self.actif = 0
                                self.tempsrecharge += 1
                def lancer(self):
                        if self.dispo:
                                player.defense += 4
                                self.dispo = 0
                                self.actif = 1
                                
        class Arme_Enflammee:
                def __init__(self):
                        self.duree = 7 + player.magie
                        self.recharge = 30 - player.magie
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge >= self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                        if self.tempsecoule >= self.duree:
                                player.attaque -= 4
                                player.degat -= 1
                                self.actif = 0
                                self.tempsrecharge += 1
                def lancer(self):
                        if self.dispo:
                                player.attaque +=4
                                player.degat += 1
                                self.dispo = 0
                                self.actif = 1
                                
        class Invisibilite:
                def __init__(self):
                        self.duree = 10 + player.magie
                        self.recharge = 10 - player.magie
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge >= self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                        if self.tempsecoule >= self.duree:
                                player.discretion -= 30
                                self.actif = 0
                                self.tempsrecharge += 1
                def lancer(self):
                        if self.dispo:
                                player.discretion += 30
                                self.dispo = 0
                                self.actif = 1
                                
        class Soin:
                def __init__(self):
                        self.recharge = 50 - player.magie
                        self.dispo = 1
                        self.tempsrecharge = 0
                def update(self):
                        if not self.dispo:
                                self.tempsrecharge += 1
                        if self.tempsrecharge == self.recharge:
                                self.dispo = 1
                                self.tempsrecharge = 0
                def lancer(self):
                        if self.dispo:
                                player.pv = player.pvmax
                                self.dispo = 0    
                                
                        
                                
                                
                        
player = Player()

spellslist = []
berserk = Spell.Berserk()
corps_dacier = Spell.Corps_Dacier()
arme_enflammee = Spell.Arme_Enflammee()
invisibilite = Spell.Invisibilite()
soin = Spell.Soin()

spellslist.extend((berserk,corps_dacier,arme_enflammee,invisibilite,soin))

def spellsupdate():
    for Spell in spellslist:
        Spell.update()

mobslist = list()
loup1N1 = Mobs.Loup(11,8)
loup2N1 = Mobs.Loup(41,10)
loup3N1 = Mobs.Loup(36,22)
loup4N1 = Mobs.Loup(12,23)
loup5N1 = Mobs.Loup(42,25)
loup6N1 = Mobs.Loup(12,27)
loup7N1 = Mobs.Loup(47,29)
loup8N1 = Mobs.Loup(43,37)
loup9N1 = Mobs.Loup(16,41)
loup10N1 = Mobs.Loup(25,45)
loup1N2 = Mobs.Loup(27,40)
loup2N2 = Mobs.Loup(32,40)
loup1N4 = Mobs.Loup(22,9)
loup2N4 = Mobs.Loup(34,43)
loup3N4 = Mobs.Loup(39,49)
loup1N5 = Mobs.Loup(23,43)
loup2N5 = Mobs.Loup(27,43)
loup3N5 = Mobs.Loup(31,43)
loup4N5 = Mobs.Loup(32,43)
mobslist.append(map(lambda x : x[1], filter(lambda x : x[0].startswith('loup'), globals().items())))
squelette1N2 = Mobs.Squelette(39,7)
squelette2N2 = Mobs.Squelette(48,10)
squelette3N2 = Mobs.Squelette(40,13)
squelette4N2 = Mobs.Squelette(48,16)
squelette5N2 = Mobs.Squelette(30,35)
squelette6N2 = Mobs.Squelette(39,41)
squelette7N2 = Mobs.Squelette(41,44)
squelette1N3 = Mobs.Squelette(28,25)
squelette2N3 = Mobs.Squelette(35,26)
squelette3N3 = Mobs.Squelette(46,26)
squelette4N3 = Mobs.Squelette(28,29)
squelette5N3 = Mobs.Squelette(33,30)
squelette6N3 = Mobs.Squelette(43,34)
squelette7N3 = Mobs.Squelette(13,41)
squelette1N4 = Mobs.Squelette(9,8)
squelette2N4 = Mobs.Squelette(30,17)
squelette3N4 = Mobs.Squelette(37,17)
squelette4N4 = Mobs.Squelette(16,32)
squelette5N4 = Mobs.Squelette(25,32)
squelette6N4 = Mobs.Squelette(13,36)
squelette7N4 = Mobs.Squelette(22,36)
squelette8N4 = Mobs.Squelette(44,39)
squelette1N5 = Mobs.Squelette(8,13)
squelette2N5 = Mobs.Squelette(48,13)
squelette3N5 = Mobs.Squelette(18,18)
squelette4N5 = Mobs.Squelette(8,19)
mobslist.append(map(lambda x : x[1], filter(lambda x : x[0].startswith('squelette'), globals().items())))
centaure1N2 = Mobs.Centaure(21,19)
centaure2N2 = Mobs.Centaure(23,27)
centaure1N3 = Mobs.Centaure(8,8)
centaure2N3 = Mobs.Centaure(37,41)
centaure3N3 = Mobs.Centaure(23,44)
centaure4N3 = Mobs.Centaure(51,44)
centaure1N4 = Mobs.Centaure(26,23)
centaure2N4 = Mobs.Centaure(32,23)
centaure3N4 = Mobs.Centaure(35,37)
centaure1N5 = Mobs.Centaure(36,27)
centaure2N5 = Mobs.Centaure(19,28)
mobslist.append(map(lambda x : x[1], filter(lambda x : x[0].startswith('centaure'), globals().items())))
cavalier1N2 = Mobs.Cavalier(8,8)
cavalier1N4 = Mobs.Cavalier(30,12)
cavalier2N4 = Mobs.Cavalier(14,13)
cavalier3N4 = Mobs.Cavalier(46,16)
cavalier4N4 = Mobs.Cavalier(30,25)
cavalier5N4 = Mobs.Cavalier(44,34)
cavalier6N4 = Mobs.Cavalier(14,39)
cavalier1N5 = Mobs.Cavalier(18,20)
cavalier2N5 = Mobs.Cavalier(35,20)
cavalier3N5 = Mobs.Cavalier(28,23)
mobslist.append(map(lambda x : x[1], filter(lambda x : x[0].startswith('cavalier'), globals().items())))
mort_vivant1N2 = Mobs.Mort_vivant(45,7)
mort_vivant2N2 = Mobs.Mort_vivant(51,13)
mort_vivant3N2 = Mobs.Mort_vivant(44,19)
mort_vivant4N2 = Mobs.Mort_vivant(51,22)
mort_vivant5N2 = Mobs.Mort_vivant(43,31)
mort_vivant6N2 = Mobs.Mort_vivant(38,34)
mort_vivant7N2 = Mobs.Mort_vivant(45,34)
mort_vivant8N2 = Mobs.Mort_vivant(8,39)
mort_vivant9N2 = Mobs.Mort_vivant(49,44)
mort_vivant10N2 = Mobs.Mort_vivant(44,46)
mort_vivant1N3 = Mobs.Mort_vivant(8,45)
mort_vivant1N4 = Mobs.Mort_vivant(16,21)
mort_vivant2N4 = Mobs.Mort_vivant(19,45)
mort_vivant1N5 = Mobs.Mort_vivant(11,24)
mort_vivant2N5 = Mobs.Mort_vivant(48,24)
mobslist.append(map(lambda x : x[1], filter(lambda x : x[0].startswith('mort_vivant'), globals().items())))
araignee1N2 = Mobs.Araignee(13,9)
araignee2N2 = Mobs.Araignee(9,10)
araignee3N2 = Mobs.Araignee(27,21)
araignee4N2 = Mobs.Araignee(33,23)
araignee5N2 = Mobs.Araignee(23,24)
araignee6N2 = Mobs.Araignee(33,27)
araignee7N2 = Mobs.Araignee(25,29)
araignee8N2 = Mobs.Araignee(29,29)
araignee9N2 = Mobs.Araignee(10,37)
araignee10N2 = Mobs.Araignee(10,42)
araignee1N3 = Mobs.Araignee(30,21)
araignee2N3 = Mobs.Araignee(30,27)
araignee1N4 = Mobs.Araignee(21,43)
araignee2N4 = Mobs.Araignee(49,46)
araignee1N5 = Mobs.Araignee(15,40)
araignee2N5 = Mobs.Araignee(42,40)
araignee3N5 = Mobs.Araignee(10,41)
araignee4N5 = Mobs.Araignee(50,42)
mobslist.append(map(lambda x : x[1], filter(lambda x : x[0].startswith('araignee'), globals().items())))
orc1N1 = Mobs.Orc(47,18)
orc2N1 = Mobs.Orc(30,29)
orc3N1 = Mobs.Orc(14,32)
orc4N1 = Mobs.Orc(28,10)
orc5N1 = Mobs.Orc(34,13)
orc6N1 = Mobs.Orc(11,17)
orc1N3 = Mobs.Orc(43,13)
orc2N3 = Mobs.Orc(41,17)
orc3N3 = Mobs.Orc(48,17)
orc4N3 = Mobs.Orc(49,24)
orc5N3 = Mobs.Orc(41,26)
orc6N3 = Mobs.Orc(48,30)
orc7N3 = Mobs.Orc(50,34)
orc8N3 = Mobs.Orc(49,37)
orc1N4 = Mobs.Orc(46,8)
orc2N4 = Mobs.Orc(16,17)
orc1N4 = Mobs.Orc(49,36)
orc2N5 = Mobs.Orc(13,33)
orc3N5 = Mobs.Orc(36,33)
mobslist.append(map(lambda x : x[1], filter(lambda x : x[0].startswith('orc'), globals().items())))
gobelin1N2 = Mobs.Gobelin(9,18)
gobelin2N2 = Mobs.Gobelin(9,21)
gobelin3N2 = Mobs.Gobelin(17,33)
gobelin4N2 = Mobs.Gobelin(20,33)
gobelin5N2 = Mobs.Gobelin(17,35)
gobelin6N2 = Mobs.Gobelin(20,35)
gobelin1N3 = Mobs.Gobelin(13,14)
gobelin2N3 = Mobs.Gobelin(10,18)
gobelin3N3 = Mobs.Gobelin(17,19)
gobelin4N3 = Mobs.Gobelin(14,23)
gobelin5N3 = Mobs.Gobelin(20,27)
gobelin6N3 = Mobs.Gobelin(8,28)
gobelin7N3 = Mobs.Gobelin(14,29)
gobelin8N3 = Mobs.Gobelin(19,32)
gobelin9N3 = Mobs.Gobelin(15,36)
gobelin10N3 = Mobs.Gobelin(10,38)
gobelin1N4 = Mobs.Gobelin(7,7)
gobelin2N4 = Mobs.Gobelin(21,24)
gobelin3N4 = Mobs.Gobelin(47,25)
gobelin4N4 = Mobs.Gobelin(40,26)
gobelin5N4 = Mobs.Gobelin(40,29)
gobelin6N4 = Mobs.Gobelin(46,29)
mobslist.append(map(lambda x : x[1], filter(lambda x : x[0].startswith('gobelin'), globals().items())))
persephon = Mobs.Persephon(29,16)
mobslist.append(persephon)

def mobsupdate():
    for Mobs in mobslist:
        Mobs.update()


def update():
    mobsupdate()
    spellsupdate()
    player.update()



#initialisation des polices d'ecriture
font = pygame.font.SysFont("Chiller", 40)
font2 = pygame.font.SysFont("Chiller", 70)
font3 = pygame.font.SysFont("Chiller",48)

#rendre tous les sorts disponibles
berserk = 1
affichage_be="disponible"
corps_d_acier=1
affichage_ca="disponible"
arme_d_acier = 1
affichage_aa="disponible"
invisibilite = 1
affichage_in="disponible"
soin = 1
affichage_soin="disponible"

def hud():
        #mise en place du fond
        fond = pygame.image.load("Images/Hud.jpg").convert()
        fenetre.blit(fond,(0,0))
        #ecriture des textes
        rendu_pv = font.render("PV :", 1, (255,0,0))
        fenetre.blit(rendu_pv,(100,10))
        point_vie = font.render(str(player.pv),1,(255,0,0))
        slash = font.render("/",1,(255,0,0))
        point_vie_max=font.render(str(player.pvmax),1,(255,0,0))
        fenetre.blit(point_vie,(70,70))
        fenetre.blit(point_vie_max,(160,70))
        fenetre.blit(slash,(120,70))
        ecris_niveau =font.render("Niveau",1,(255,0,0))
        niveau = font.render(str(player.level),1,(255,0,0))
        fenetre.blit(ecris_niveau,(80,130))
        fenetre.blit(niveau,(180,130))
        ecris_xp=font.render("XP :",1,(255,0,0))
        experience = font.render(str(player.xp), 1, (255,0,0))
        experience_demandee =font.render(str(player.nextlevelxp), 1, (255,0,0))
        fenetre.blit(ecris_xp,(100,180))
        fenetre.blit(experience,(70,230))
        fenetre.blit(experience_demandee,(160,230))
        fenetre.blit(slash,(120,230))
        ecrit_be= font.render ("Berserk-touche 1",1,(255,0,0))
        fenetre.blit(ecrit_be,(30,310))
        dispo_be = font.render(str(affichage_be),1,(172,35,220))
        fenetre.blit(dispo_be,(100,340))
        ecrit_ca = font.render ("Corps d'acier-touche 2",1,(255,0,0))
        fenetre.blit(ecrit_ca,(0,410))
        dispo_ca = font.render(str(affichage_ca),1,(172,35,220))
        fenetre.blit(dispo_ca,(100,440))
        ecrit_aa = font.render ("Arme d'acier-touche 3",1,(255,0,0))
        fenetre.blit(ecrit_aa,(0,510))
        dispo_aa = font.render(str(affichage_aa),1,(172,35,220))
        fenetre.blit(dispo_aa,(100,540))
        ecrit_in = font.render ("Invisibilite-touche 4",1,(255,0,0))
        fenetre.blit(ecrit_in,(30,610))
        dispo_in = font.render(str(affichage_in),1,(172,35,220))
        fenetre.blit(dispo_in,(100,640))
        ecrit_soin = font.render ("Soin-touche 5",1,(255,0,0))
        fenetre.blit(ecrit_soin,(70,710))
        dispo_soin = font.render(str(affichage_soin),1,(172,35,220))
        fenetre.blit(dispo_soin,(100,740))
