#Classe du joueur
import pygame
pygame.init()
from random import *
from pygame.locals import*
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
                self.up = pygame.image.load("Hero-up.png")
                self.down = pygame.image.load("Hero-down.png")
                self.left = pygame.image.load("Hero-left.png")
                self.right = pygame.image.load("Hero-right.png")
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
                                player.xp += self.xp
                                del(self)
                        if player.x = self.x or player.y = self.y:
                                if player.y - 1 = self.y
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 = self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 = self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 = self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y = self.y or Mobs.x = self.x:
                                                if Mobs.y - 1 = self.y or Mobs.y + 1 = self.y or Mobs.x - 1 = self.x or Mobs.x + 1 = self.x:
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
                        if structure_niveau[self.y][self.x-1]='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]='h':
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
                                player.xp += self.xp
                                del(self)
                        if player.x = self.x or player.y = self.y:
                                if player.y - 1 = self.y
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 = self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 = self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 = self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y = self.y or Mobs.x = self.x:
                                                if Mobs.y - 1 = self.y or Mobs.y + 1 = self.y or Mobs.x - 1 = self.x or Mobs.x + 1 = self.x:
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
                        if structure_niveau[self.y][self.x-1]='h':
                                self.x -= 1
                def moveright(self):
                        if structure_niveau[self.y][self.x+1]='h':
                                self.x += 1
                def moveup(self):
                        if structure_niveau[self.y-1][self.x]='h':
                                self.y -= 1
                def movedown(self):
                        if structure_niveau[self.y+1][self.x]='h':
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
                                player.xp += self.xp
                                del(self)
                        if player.x = self.x or player.y = self.y:
                                if player.y - 1 = self.y
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 = self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 = self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 = self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y = self.y or Mobs.x = self.x:
                                                if Mobs.y - 1 = self.y or Mobs.y + 1 = self.y or Mobs.x - 1 = self.x or Mobs.x + 1 = self.x:
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
        class Centaure:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
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
                                player.xp += self.xp
                                del(self)
                        if player.x = self.x or player.y = self.y:
                                if player.y - 1 = self.y
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 = self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 = self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 = self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y = self.y or Mobs.x = self.x:
                                                if Mobs.y - 1 = self.y or Mobs.y + 1 = self.y or Mobs.x - 1 = self.x or Mobs.x + 1 = self.x:
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
        class Mort_vivant:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
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
                                player.xp += self.xp
                                del(self)
                        if player.x = self.x or player.y = self.y:
                                if player.y - 1 = self.y
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 = self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 = self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 = self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y = self.y or Mobs.x = self.x:
                                                if Mobs.y - 1 = self.y or Mobs.y + 1 = self.y or Mobs.x - 1 = self.x or Mobs.x + 1 = self.x:
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
        class Squelette:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
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
                                player.xp += self.xp
                                del(self)
                        if player.x = self.x or player.y = self.y:
                                if player.y - 1 = self.y
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 = self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 = self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 = self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y = self.y or Mobs.x = self.x:
                                                if Mobs.y - 1 = self.y or Mobs.y + 1 = self.y or Mobs.x - 1 = self.x or Mobs.x + 1 = self.x:
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
        class Araignee:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
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
                                player.xp += self.xp
                                del(self)
                        if player.x = self.x or player.y = self.y:
                                if player.y - 1 = self.y
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 = self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 = self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 = self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y = self.y or Mobs.x = self.x:
                                                if Mobs.y - 1 = self.y or Mobs.y + 1 = self.y or Mobs.x - 1 = self.x or Mobs.x + 1 = self.x:
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
        class Persephon:
                def __init__(self,x,y):
                        self.x = x
                        self.y = y
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
                                player.xp += self.xp
                                del(self)
                        if player.x = self.x or player.y = self.y:
                                if player.y - 1 = self.y
                                        adjacent_bas = self
                                        self.attack(player)
                                if player.y + 1 = self.y:
                                        adjacent_haut = self
                                        self.attack(player)
                                if player.x - 1 = self.x:
                                        adjacent_droite = self
                                        self.attack(player)
                                if player.x + 1 = self.x:
                                        adjacent_gauche = self
                                        self.attack(player)
                        else:
                                for Mobs in mobslist:
                                        if Mobs.y = self.y or Mobs.x = self.x:
                                                if Mobs.y - 1 = self.y or Mobs.y + 1 = self.y or Mobs.x - 1 = self.x or Mobs.x + 1 = self.x:
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
                        player.attaque += 2
                        player.vitesse += 2
                        player.degat += 1
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge == self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                        if self.tempsecoule >= self.duree:
                                player.attaque -= 2
                                player.vitesse -= 2
                                player.degat -= 1
                                self.actif = 0
                                self.tempsrecharge += 1
        class Corps_Dacier:
                def __init__(self):
                        self.duree = 7 + player.magie
                        self.recharge = 30 - player.magie
                        player.defense += 4
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge == self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                        if self.tempsecoule >= self.duree:
                                player.defense -= 4
                                self.actif = 0
                                self.tempsrecharge += 1
                                
        class Arme_Enflammee:
                def __init__(self):
                        self.duree = 7 + player.magie
                        self.recharge = 30 - player.magie
                        player.attaque += 4
                        player.degat += 1
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge == self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                        if self.tempsecoule >= self.duree:
                                player.attaque -= 4
                                player.degat -= 1
                                self.actif = 0
                                self.tempsrecharge += 1
                                
        class Invisibilite:
                def __init__(self):
                        self.duree = 10 + player.magie
                        self.recharge = 10 - player.magie
                        player.discretion += 30
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge == self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                        if self.tempsecoule >= self.duree:
                                player.discretion -= 30
                                self.actif = 0
                                self.tempsrecharge += 1
                                
        class Soin:
                def __init__(self):
                        self.recharge = 50 - player.magie
                        player.pv = player.pvmax
                        self.dispo = 1
                        self.tempsrecharge = 0
                def update(self):
                        if not self.dispo:
                                self.tempsrecharge += 1
                        if self.tempsrecharge == self.recharge:
                                self.dispo = 1
                                self.tempsrecharge = 0
                                
                        
                                
                                
                        
