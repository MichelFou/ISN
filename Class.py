#Classe du joueur
import pygame
pygame.init()
from random import *
from pygame.locals import*
from bibliotheque import *
import actions

fenetre = pygame.display.set_mode((1083,812))

a = pygame.image.load("Images/Hero-up.png")
b = pygame.image.load("Images/Hero-down.png")
c = pygame.image.load("Images/Hero-left.png")
d = pygame.image.load("Images/Hero-right.png")
Niveau = 0


with open("carte.txt", "r")as fichier:
    for ligne in fichier:
        for sprite in ligne:
            if sprite =="1":
                Niveau = 1
            if sprite =="2":
                Niveau = 2
            if sprite == "3":
                Niveau = 3
            if sprite == "4":
                Niveau = 4
            if sprite=="5":
                Niveau = 5

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
                self.nextlevel = False
                self.image = a
                self.valeur = 0
                
        def moveup(self):
                self.image = a
                self.y-=1

        def movedown(self):
                self.image = b
                self.y+=1

        def moveleft(self):
                self.image = c
                self.x-=1
        
        def moveright(self):
                self.image = d
                self.x+=1

        def levelup(self):
                self.pv += 5
                self.pvmax += 5
                self.attaque += 1
                self.defense += 1
                self.vitesse += 1
                self.magie += 1
                self.degat += 1
                self.discretion += 1
                self.nextlevel = False

        def update(self):
                if self.xp == self.nextlevelxp:
                        self.xp = 0
                        self.levelup = True
                if self.xp > self.nextlevelxp:
                        self.xp -= self.nextlevelxp
                        self.nextlevel = True
                if self.nextlevel:
                        self.levelup()
                if self.pv <= 0:
                    self.estmort = True
        
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

        def blesse(self,name):
                if randint(1,30)<name.attaque:
                        if randint(1,30)>self.vitesse:
                                self.valeur = randint(1,name.degat)-randint(1,self.defense)
                                if self.valeur > 0:
                                        self.pv -= self.valeur
                                        rendu_valeur = font.render(str(-self.valeur),1,(255,255,255))
                                        with open("carte.txt", "r")as fichier:
                                            for ligne in fichier:
                                                for sprite in ligne:
                                                    if sprite =="1":
                                                        mobslist = mobsN1
                                                    if sprite =="2":
                                                        mobslist = mobsN2
                                                    if sprite == "3":
                                                        mobslist = mobsN3
                                                    if sprite == "4":
                                                        mobslist = mobsN4
                                                    if sprite=="5":
                                                        mobslist = mobsN5
                                        for i in range(0,500):
                                            fenetre.blit(self.image,(640,360))
                                            for mobs in mobslist:
                                                if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                                    fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                                    fenetre.blit(rendu_valeur,(670,320))
                                            pygame.display.flip()
                                            
                                else:
                                        self.pv -= 0
                        else:
                            with open("carte.txt", "r")as fichier:
                                for ligne in fichier:
                                    for sprite in ligne:
                                        if sprite =="1":
                                            mobslist = mobsN1
                                        if sprite =="2":
                                            mobslist = mobsN2
                                        if sprite == "3":
                                            mobslist = mobsN3
                                        if sprite == "4":
                                            mobslist = mobsN4
                                        if sprite=="5":
                                            mobslist = mobsN5
                            for i in range(0,500):
                                fenetre.blit(self.image,(640,360))
                                for mobs in mobslist:
                                    if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                        fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                        rendu_esquive = font.render("Esquive!",1,(255,255,255))
                                        fenetre.blit(rendu_esquive,(670,320))
                                pygame.display.flip()
                else:
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    mobslist = mobsN1
                                if sprite =="2":
                                    mobslist = mobsN2
                                if sprite == "3":
                                    mobslist = mobsN3
                                if sprite == "4":
                                    mobslist = mobsN4
                                if sprite=="5":
                                    mobslist = mobsN5
                    for i in range(0,500):
                        fenetre.blit(self.image,(640,360))
                        for mobs in mobslist:
                            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                    fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                    rendu_echec = font.render("Echec!",1,(51,0,0))
                                    fenetre.blit(rendu_echec,(660+(self.x-player.x)*72,320+(self.y-player.y)*72))
                        pygame.display.flip()
                if self.pv <= 0:
                    self.estmort = True
        def attack(self,name):
                name.blesse(self)

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
                self.move = False
                self.mobslist = []
                self.niveau = 1
        def update(self):
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
                                diffx = abs(player.x-self.x)
                                diffy = abs(player.y-self.y)
                                if diffx > diffy:
                                    if self.x > player.x:
                                        self.moveleft()
                                    elif self.x < player.x:
                                        self.moveright()
                                elif diffy > diffx:
                                    if self.y > player.y:
                                        self.moveup()
                                    elif self.y < player.y:
                                        self.movedown()
                                elif diffy == diffx:
                                    if self.x > player.x:
                                        self.moveleft()
                                    elif self.x < player.x:
                                        self.moveright()
                                    elif self.y > player.y:
                                        self.moveup()
                                    elif self.y < player.y:
                                        self.movedown()
        def moveleft(self):
                move = 0
                with open("carte.txt", "r")as fichier:
                    for ligne in fichier:
                        for sprite in ligne:
                            if sprite =="1":
                                carte = actions.carte1
                                mobslist = mobsN1
                            if sprite =="2":
                                carte = actions.carte2
                                mobslist = mobsN2
                            if sprite == "3":
                                carte = actions.carte3
                                mobslist = mobsN3
                            if sprite == "4":
                                carte = actions.carte4
                                mobslist = mobsN4
                            if sprite=="5":
                                carte = actions.carte5
                                mobslist = mobsN5
                for mobs in mobslist:
                    if self.x-1 == mobs.x and self.y == mobs.y:
                        move+=1
                if carte.structure[self.y][self.x-1]=='h' and move==0:
                        self.x -= 1
                    
        def moveright(self):
                move = 0
                with open("carte.txt", "r")as fichier:
                    for ligne in fichier:
                        for sprite in ligne:
                            if sprite =="1":
                                carte = actions.carte1
                                mobslist = mobsN1
                            if sprite =="2":
                                carte = actions.carte2
                                mobslist = mobsN2
                            if sprite == "3":
                                carte = actions.carte3
                                mobslist = mobsN3
                            if sprite == "4":
                                carte = actions.carte4
                                mobslist = mobsN4
                            if sprite=="5":
                                carte = actions.carte5
                                mobslist = mobsN5
                for mobs in mobslist:
                    if self.x+1 == mobs.x and self.y == mobs.y:
                        move+=1
                if carte.structure[self.y][self.x+1]=='h' and move==0:
                        self.x += 1
        def moveup(self):
                move = 0
                with open("carte.txt", "r")as fichier:
                    for ligne in fichier:
                        for sprite in ligne:
                            if sprite =="1":
                                carte = actions.carte1
                                mobslist = mobsN1
                            if sprite =="2":
                                carte = actions.carte2
                                mobslist = mobsN2
                            if sprite == "3":
                                carte = actions.carte3
                                mobslist = mobsN3
                            if sprite == "4":
                                carte = actions.carte4
                                mobslist = mobsN4
                            if sprite=="5":
                                carte = actions.carte5
                                mobslist = mobsN5
                for mobs in mobslist:
                    if self.x == mobs.x and self.y-1 == mobs.y:
                        move+=1
                if carte.structure[self.y-1][self.x]=='h' and move==0:
                        self.y -= 1
        def movedown(self):
                move = 0
                with open("carte.txt", "r")as fichier:
                    for ligne in fichier:
                        for sprite in ligne:
                            if sprite =="1":
                                carte = actions.carte1
                                mobslist = mobsN1
                            if sprite =="2":
                                carte = actions.carte2
                                mobslist = mobsN2
                            if sprite == "3":
                                carte = actions.carte3
                                mobslist = mobsN3
                            if sprite == "4":
                                carte = actions.carte4
                                mobslist = mobsN4
                            if sprite=="5":
                                carte = actions.carte5
                                mobslist = mobsN5
                for mobs in mobslist:
                    if self.x == mobs.x and self.y+1 == mobs.y:
                        move+=1
                if carte.structure[self.y+1][self.x]=='h' and move==0:
                        self.x += 1

        def blesse(self,name):
                if randint(1,30)<name.attaque:
                        if randint(1,30)>self.vitesse:
                                self.valeur = randint(1,name.degat)-randint(1,self.defense)
                                if self.valeur > 0:
                                        self.pv -= self.valeur
                                        rendu_valeur = font.render(str(-self.valeur),1,(51,0,0))
                                        with open("carte.txt", "r")as fichier:
                                            for ligne in fichier:
                                                for sprite in ligne:
                                                    if sprite =="1":
                                                        mobslist = mobsN1
                                                    if sprite =="2":
                                                        mobslist = mobsN2
                                                    if sprite == "3":
                                                        mobslist = mobsN3
                                                    if sprite == "4":
                                                        mobslist = mobsN4
                                                    if sprite=="5":
                                                        mobslist = mobsN5
                                        for i in range(0,500):
                                            for mobs in mobslist:
                                                if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                                    fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                            fenetre.blit(player.image,(640,360))
                                            fenetre.blit(rendu_valeur,(660+(self.x-player.x)*72,320+(self.y-player.y)*72))

                                            

                                            pygame.display.flip()
                                else:
                                        self.pv -= 0
                        else:
                            with open("carte.txt", "r")as fichier:
                                for ligne in fichier:
                                    for sprite in ligne:
                                        if sprite =="1":
                                            mobslist = mobsN1
                                        if sprite =="2":
                                            mobslist = mobsN2
                                        if sprite == "3":
                                            mobslist = mobsN3
                                        if sprite == "4":
                                            mobslist = mobsN4
                                        if sprite=="5":
                                            mobslist = mobsN5
                            for i in range(0,500):
                                fenetre.blit(player.image,(640,360))
                                for mobs in mobslist:
                                    if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                        fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                        rendu_esquive = font.render("Esquive!",1,(255,0,0))
                                        fenetre.blit(rendu_esquive,(660+(self.x-player.x)*72,320+(self.y-player.y)*72))
                                pygame.display.flip()
                else:
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    mobslist = mobsN1
                                if sprite =="2":
                                    mobslist = mobsN2
                                if sprite == "3":
                                    mobslist = mobsN3
                                if sprite == "4":
                                    mobslist = mobsN4
                                if sprite=="5":
                                    mobslist = mobsN5
                    for i in range(0,500):
                        fenetre.blit(player.image,(640,360))
                        for mobs in mobslist:
                            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                    fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                    rendu_echec = font.render("Echec!",1,(255,0,0))
                                    fenetre.blit(rendu_echec,(670,320))
                        pygame.display.flip()
                        
                if self.pv <= 0:
                    player.xp += self.xp
                    if self.niveau == 1:
                        mobsN1.remove(self)
                    if self.niveau == 2:
                        mobsN2.remove(self)
                    if self.niveau == 3:
                        mobsN3.remove(self)
                    if self.niveau == 4:
                        mobsN4.remove(self)
                    if self.niveau == 5:
                        mobsN5.remove(self)
                    del(self)

        def attack(self,name):
                name.blesse(self)
        
class Loup(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1
class Orc(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1
class Gobelin(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1
class Centaure(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1
class Mort_vivant(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1
class Squelette(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1
class Araignee(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1
class Persephon(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1

class Cavalier(Mobs):
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
                self.move = False
                self.mobslist = []
                self.niveau = 1
  
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
                        self.duree = 7 + int(0.2*player.magie)
                        self.recharge = 20 - int(0.5*player.magie)
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
                        self.duree = 7 + int(0.2*player.magie)
                        self.recharge = 20 - int(0.5*player.magie)
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
                        self.duree = 7 + int(0.2*player.magie)
                        self.recharge = 20 - int(0.5*player.magie)
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
                        self.duree = 7 + int(0.2*player.magie)
                        self.recharge = 20 - int(0.5*player.magie)
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
                                
                        
                                
                                
player=Player()                       
spell = Spell()
spellslist = []
berserk = spell.Berserk()
corps_dacier = spell.Corps_Dacier()
arme_enflammee = spell.Arme_Enflammee()
invisibilite = spell.Invisibilite()
soin = spell.Soin()

spellslist.extend((berserk,corps_dacier,arme_enflammee,invisibilite,soin))

def spellsupdate():
    for spell in spellslist:
        spell.update()

mobs = Mobs()

mobsN1 = []
mobsN2 = []
mobsN3 = []
mobsN4 = []
mobsN5 = []
mobslist = []
loup1N1 = Loup(11,8)
loup2N1 = Loup(41,10)
loup3N1 = Loup(36,22)
loup4N1 = Loup(12,23)
loup5N1 = Loup(42,25)
loup6N1 = Loup(12,27)
loup7N1 = Loup(47,29)
loup8N1 = Loup(43,37)
loup9N1 = Loup(16,41)
loup10N1 = Loup(25,45)
loup1N2 = Loup(27,40)
loup2N2 = Loup(32,40)
loup1N4 = Loup(22,9)
loup2N4 = Loup(34,43)
loup3N4 = Loup(39,49)
loup1N5 = Loup(23,43)
loup2N5 = Loup(27,43)
loup3N5 = Loup(31,43)
loup4N5 = Loup(32,43)
squelette1N2 = Squelette(39,7)
squelette2N2 = Squelette(48,10)
squelette3N2 = Squelette(40,13)
squelette4N2 = Squelette(48,16)
squelette5N2 = Squelette(30,35)
squelette6N2 = Squelette(39,41)
squelette7N2 = Squelette(41,44)
squelette1N3 = Squelette(28,25)
squelette2N3 = Squelette(35,26)
squelette3N3 = Squelette(46,26)
squelette4N3 = Squelette(28,29)
squelette5N3 = Squelette(33,30)
squelette6N3 = Squelette(43,34)
squelette7N3 = Squelette(13,41)
squelette1N4 = Squelette(9,8)
squelette2N4 = Squelette(30,17)
squelette3N4 = Squelette(37,17)
squelette4N4 = Squelette(16,32)
squelette5N4 = Squelette(25,32)
squelette6N4 = Squelette(13,36)
squelette7N4 = Squelette(22,36)
squelette8N4 = Squelette(44,39)
squelette1N5 = Squelette(8,13)
squelette2N5 = Squelette(48,13)
squelette3N5 = Squelette(18,18)
squelette4N5 = Squelette(8,19)
centaure1N2 = Centaure(21,19)
centaure2N2 = Centaure(23,27)
centaure1N3 = Centaure(8,8)
centaure2N3 = Centaure(37,41)
centaure3N3 = Centaure(23,44)
centaure4N3 = Centaure(51,44)
centaure1N4 = Centaure(26,23)
centaure2N4 = Centaure(32,23)
centaure3N4 = Centaure(35,37)
centaure1N5 = Centaure(36,27)
centaure2N5 = Centaure(19,28)
cavalier1N2 = Cavalier(8,8)
cavalier1N4 = Cavalier(30,12)
cavalier2N4 = Cavalier(14,13)
cavalier3N4 = Cavalier(46,16)
cavalier4N4 = Cavalier(30,25)
cavalier5N4 = Cavalier(44,34)
cavalier6N4 = Cavalier(14,39)
cavalier1N5 = Cavalier(18,20)
cavalier2N5 = Cavalier(35,20)
cavalier3N5 = Cavalier(28,23)
mort_vivant1N2 = Mort_vivant(45,7)
mort_vivant2N2 = Mort_vivant(51,13)
mort_vivant3N2 = Mort_vivant(44,19)
mort_vivant4N2 = Mort_vivant(51,22)
mort_vivant5N2 = Mort_vivant(43,31)
mort_vivant6N2 = Mort_vivant(38,34)
mort_vivant7N2 = Mort_vivant(45,34)
mort_vivant8N2 = Mort_vivant(8,39)
mort_vivant9N2 = Mort_vivant(49,44)
mort_vivant10N2 = Mort_vivant(44,46)
mort_vivant1N3 = Mort_vivant(8,45)
mort_vivant1N4 = Mort_vivant(16,21)
mort_vivant2N4 = Mort_vivant(19,45)
mort_vivant1N5 = Mort_vivant(11,24)
mort_vivant2N5 = Mort_vivant(48,24)
araignee1N2 = Araignee(13,9)
araignee2N2 = Araignee(9,10)
araignee3N2 = Araignee(27,21)
araignee4N2 = Araignee(33,23)
araignee5N2 = Araignee(23,24)
araignee6N2 = Araignee(33,27)
araignee7N2 = Araignee(25,29)
araignee8N2 = Araignee(29,29)
araignee9N2 = Araignee(10,37)
araignee10N2 = Araignee(10,42)
araignee1N3 = Araignee(30,21)
araignee2N3 = Araignee(30,27)
araignee1N4 = Araignee(21,43)
araignee2N4 = Araignee(49,46)
araignee1N5 = Araignee(15,40)
araignee2N5 = Araignee(42,40)
araignee3N5 = Araignee(10,41)
araignee4N5 = Araignee(50,42)
orc1N1 = Orc(47,18)
orc2N1 = Orc(30,29)
orc3N1 = Orc(14,32)
orc4N1 = Orc(28,10)
orc5N1 = Orc(34,13)
orc6N1 = Orc(11,17)
orc1N3 = Orc(43,13)
orc2N3 = Orc(41,17)
orc3N3 = Orc(48,17)
orc4N3 = Orc(49,24)
orc5N3 = Orc(41,26)
orc6N3 = Orc(48,30)
orc7N3 = Orc(50,34)
orc8N3 = Orc(49,37)
orc1N4 = Orc(46,8)
orc2N4 = Orc(16,17)
orc1N5 = Orc(49,36)
orc2N5 = Orc(13,33)
orc3N5 = Orc(36,33)
gobelin1N2 = Gobelin(9,18)
gobelin2N2 = Gobelin(9,21)
gobelin3N2 = Gobelin(17,33)
gobelin4N2 = Gobelin(20,33)
gobelin5N2 = Gobelin(17,35)
gobelin6N2 = Gobelin(20,35)
gobelin1N3 = Gobelin(13,14)
gobelin2N3 = Gobelin(10,18)
gobelin3N3 = Gobelin(17,19)
gobelin4N3 = Gobelin(14,23)
gobelin5N3 = Gobelin(20,27)
gobelin6N3 = Gobelin(8,28)
gobelin7N3 = Gobelin(14,29)
gobelin8N3 = Gobelin(19,32)
gobelin9N3 = Gobelin(15,36)
gobelin10N3 = Gobelin(10,38)
gobelin1N4 = Gobelin(7,7)
gobelin2N4 = Gobelin(21,24)
gobelin3N4 = Gobelin(47,25)
gobelin4N4 = Gobelin(40,26)
gobelin5N4 = Gobelin(40,29)
gobelin6N4 = Gobelin(46,29)
persephon = Persephon(29,16)

mobsN1.extend((loup1N1,loup2N1,loup3N1,loup4N1,loup5N1,loup6N1,loup7N1,loup8N1,loup9N1,loup10N1,orc1N1,orc2N1,orc3N1,orc4N1,orc4N1,orc5N1,orc6N1))
mobsN2.extend((loup1N2,loup2N2,squelette1N2,squelette1N2,squelette3N2,squelette4N2,squelette5N2,squelette6N2,squelette7N2,centaure1N2,centaure2N2,cavalier1N2,mort_vivant1N2,mort_vivant2N2,mort_vivant3N2,mort_vivant4N2,mort_vivant5N2,mort_vivant6N2,mort_vivant7N2,mort_vivant8N2,mort_vivant9N2,mort_vivant10N2,araignee1N2,araignee2N2,araignee3N2,araignee4N2,araignee5N2,araignee6N2,araignee7N2,araignee8N2,araignee9N2,araignee10N2,gobelin1N2,gobelin2N2,gobelin3N2,gobelin4N2,gobelin5N2,gobelin6N2))
mobsN3.extend((squelette1N3,squelette2N3,squelette3N3,squelette4N3,squelette5N3,squelette6N3,squelette7N3,centaure1N3,centaure2N3,centaure3N3,centaure4N3,mort_vivant1N3,araignee1N3,araignee2N3,orc1N3,orc2N3,orc3N3,orc4N3,orc5N3,orc6N3,orc7N3,orc8N3,gobelin1N3,gobelin2N3,gobelin3N3,gobelin4N3,gobelin5N3,gobelin6N3,gobelin7N3,gobelin8N3,gobelin9N3,gobelin10N3))
mobsN4.extend((loup1N4,loup2N4,loup3N4,squelette1N4,squelette2N4,squelette3N4,squelette4N4,squelette5N4,squelette6N4,squelette7N4,squelette8N4,centaure1N4,centaure2N4,centaure3N4,cavalier1N4,cavalier2N4,cavalier3N4,cavalier4N4,cavalier5N4,cavalier6N4,mort_vivant1N4,mort_vivant2N4,araignee1N4,araignee2N4,orc1N4,orc2N4,gobelin1N4,gobelin2N4,gobelin3N4,gobelin4N4,gobelin5N4,gobelin6N4))
mobsN5.extend((loup1N5,loup2N5,loup3N5,loup4N5,squelette1N5,squelette2N5,squelette3N5,squelette4N5,centaure1N5,centaure2N5,cavalier1N5,cavalier2N5,cavalier3N5,mort_vivant1N5,mort_vivant2N5,araignee1N5,araignee2N5,araignee3N5,araignee4N5,orc1N5,orc2N5,orc3N5,persephon))



def mobsN1update():
    for mobs in mobsN1:
        mobs.update()
def mobsN2update():
    for mobs in mobsN2:
        mobs.update()
def mobsN3update():
    for mobs in mobsN3:
        mobs.update()
def mobsN4update():
    for mobs in mobsN4:
        mobs.update()
def mobsN5update():
    for mobs in mobsN5:
        mobs.update()

def mobsniveau():
        if Niveau == 1:
                mobslist = mobsN1
        if Niveau == 2:
                mobslist = mobsN2
        if Niveau == 3:
                mobslist = mobsN3
        if Niveau == 4:
                mobslist = mobsN4
        if Niveau == 5:
                mobslist = mobsN5


def update():
    with open("carte.txt", "r")as fichier:
        for ligne in fichier:
            for sprite in ligne:
                if sprite =="1":
                    actions.carte1.afficher(fenetre)
                    Niveau = 1
                if sprite =="2":
                    actions.carte2.afficher(fenetre)
                    Niveau = 2
                if sprite == "3":
                    actions.carte3.afficher(fenetre)
                    Niveau = 3
                if sprite == "4":
                    actions.carte4.afficher(fenetre)
                    Niveau = 4
                if sprite=="5":
                    actions.carte5.afficher(fenetre)
                    Niveau = 5
    if Niveau == 1:
            mobsN1update()
    if Niveau == 2:
            mobsN2update()
    if Niveau == 3:
            mobsN3update()
    if Niveau == 4:
            mobsN4update()
    if Niveau == 5:
            mobsN5update()
    spellsupdate()
    player.update()



#initialisation des polices d'ecriture
font = pygame.font.SysFont("Gabriola", 40)
font2 = pygame.font.SysFont("Gabriola", 70)
font3 = pygame.font.SysFont("Gabriola",48)
Trapped = pygame.font.SysFont("Gabriola",110)

#rendre tous les sorts disponibles
affichage_be="disponible"
affichage_ca="disponible"
affichage_aa="disponible"
affichage_in="disponible"
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
