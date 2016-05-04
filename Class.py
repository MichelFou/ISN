#Class des monstres, du joueur, de la carte et definitions
import pygame
pygame.init()
from random import *
from pygame.locals import*
from bibliotheque import *

#Creation d'une fenetre pour pouvoir charger des images
fenetre = pygame.display.set_mode((1083,812))

#Mise en place du niveau
def_niveau = open("carte.txt", "w")
def_niveau.write("1")
def_niveau.close()

#Chargement dans des variables des differentes images du joueur
a = pygame.image.load("Images/Hero-up.png")
b = pygame.image.load("Images/Hero-down.png")
c = pygame.image.load("Images/Hero-left.png")
d = pygame.image.load("Images/Hero-right.png")

#affichage de la map
class Niveau:
    #initialisation
    def __init__(self,fichier):
        self.fichier = fichier
        self.structure = 0
    def generer(self):
        #ouverture du fichier dee niveau demande
        with open(self.fichier, "r")as fichier:
            #creation liste structure
            structure_niveau=[]
            #lecture dans les lignes du fichier
            for ligne in fichier:
                #creation d'une liste des lignes
                ligne_niveau=[]
                #lecture de chaque sprite
                for sprite in ligne:
                    if sprite != '\n':
                        #on ajoute le sprite a la fin de la liste ligne_niveau
                        ligne_niveau.append(sprite)
                #on ajoute cette liste a la fin de structure_niveau
                structure_niveau.append(ligne_niveau)
        #on sauvegarde la liste structure_niveau
        self.structure = structure_niveau
    def afficher(self, fenetre):
        #on initialise toutes les images
        gauche= pygame.image.load("Images/Fence - side-left.png").convert_alpha()
        droite= pygame.image.load("Images/Fence - side-right.png").convert_alpha()
        milieu= pygame.image.load("Images/Fence - front-middle.png").convert_alpha()
        coin_gauche= pygame.image.load("Images/Fence - front-left.png").convert_alpha()
        coin_droite= pygame.image.load("Images/Fence - front-right.png").convert_alpha()
        tree = pygame.image.load("Images/tree.png").convert_alpha()
        herbe = pygame.image.load("Images/grass.png").convert_alpha()
        end = pygame.image.load("Images/arrive.png").convert_alpha()
        rien = pygame.image.load("Images/rien.png").convert_alpha()
        ligne_affichee = 0
        num_ligne = 0
        #on lit chaque ligne de self structure
        for ligne in self.structure:
            #si la ligne est situee a 6 sur l'axe des y du heros on continue ce qui definit un champs de vision
            if num_ligne>player.y -6 and num_ligne<player.y+6:
                case_affichee = 0
                num_sprite = 0
                #on lit dans les sprites
                for sprite in ligne:
                    #on definit x et y en fonction de la taille des sprites
                    x=(case_affichee* taille_sprite)+280
                    y=(ligne_affichee* taille_sprite)+10
                    #si le sprite est situe a 6 sur l'axe des x on continue cela definit completemnt le champ de vision
                    if num_sprite>player.x -6 and num_sprite<player.x+6:
                        #on teste pour chaque sprite quelle lettre pour savoir quel ennemi ou texture afficher
                        if sprite =='m':
                            fenetre.blit(milieu,(x,y))
                        elif sprite =='d':
                            fenetre.blit(droite,(x,y))
                        elif sprite =='g':
                            fenetre.blit(gauche,(x,y))
                        elif sprite =='l':
                            fenetre.blit(coin_gauche,(x,y))
                        elif sprite =='c':
                            fenetre.blit(coin_droite,(x,y))
                        elif sprite =='h':
                            fenetre.blit(herbe,(x,y))
                        elif sprite =='t':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(tree,(x,y))
                        elif sprite =='e':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(end,(x,y))
                        elif sprite == 'r':
                            fenetre.blit(rien,(x,y))
                        #on incremente l'endroit ou sera affichee la case
                        case_affichee = case_affichee + 1
                    #on incremente le numero du sprite teste pour evaluer si il se trouve dans le champ de vision
                    num_sprite = num_sprite + 1
                #on incremente la ligne ou sera affiche la case
                ligne_affichee = ligne_affichee+1
            #on incremente la ligne testee pour evaluer si elle est dans le champ de vision
            num_ligne = num_ligne+1


#on attribue a chaque texte de niveau une variable
carte1 = Niveau("Niveaux/N1.txt")
carte2 = Niveau("Niveaux/N2.txt")
carte3 = Niveau("Niveaux/N3.txt")
carte4 = Niveau("Niveaux/N4.txt")
carte5 = Niveau("Niveaux/N5.txt")


#Creation de la class du joueur
class Player:
        #Assignation des variables initiales
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
                self.sort = None
                self.armure = None
                self.nextlevel = False
                self.image = a
                self.valeur = 0

        #Definitions des fonctions de deplacement
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

        #Mise a jour des statistiques lors d'une montee de niveau
        def levelup(self):
                self.pv += 5
                self.pvmax += 5
                self.attaque += 1
                self.defense += 1
                self.vitesse += 1
                self.magie += 1
                self.degat += 1
                self.discretion += 1
                self.level +=1
                self.nextlevel = False
                
        #Fonction qui permet de mettre a jour l'etat du joueur
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

        #Fonctions permettant l'equipement d'armures et d'armes
        def equiper_armure(self,armure):
                self.attaque += armure.attaque
                self.defense += armure.defense
                self.discretion += armure.discretion
                self.vitesse += armure.vitesse
                self.magie += armure.magie
                stufflist.remove(armure)
                del(armure)
        
        def equiper_arme(self,arme):
                self.attaque += arme.attaque
                self.vitesse += arme.vitesse
                self.defense += arme.defense
                self.discretion += arme.discretion
                self.degat += arme.degat
                self.magie += arme.magie
                stufflist.remove(arme)
                del(arme)

        #Fonction de calcul des degats
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
                                        for i in range(0,100):
                                            fenetre.blit(self.image,(640,360))
                                            for mobs in mobslist:
                                                if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                                    fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                                    fenetre.blit(rendu_valeur,(670,320))
                                            for armure in stufflist:
                                                if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                                                    fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                                            for arme in stufflist:
                                                if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                                                    fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
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
                            #Affichage de l'esquive le cas echeant                
                            for i in range(0,100):
                                fenetre.blit(self.image,(640,360))
                                for mobs in mobslist:
                                    if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                        fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                        rendu_esquive = font.render("Esquive!",1,(255,255,255))
                                        fenetre.blit(rendu_esquive,(670,320))
                                for armure in stufflist:
                                    if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                                        fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                                for arme in stufflist:
                                    if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                                        fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
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
                    #Affichage de l'echec le cas echeant                
                    for i in range(0,100):
                        fenetre.blit(self.image,(640,360))
                        for mobs in mobslist:
                            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                    fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                    rendu_echec = font.render("Echec!",1,(51,0,0))
                                    fenetre.blit(rendu_echec,(660+(name.x-player.x)*72,320+(name.y-player.y)*72))
                        pygame.display.flip()
                if self.pv <= 0:
                    self.estmort = True
                    
        #Fonction qui permet au joueur d'attaquer
        def attack(self,name):
                name.blesse(self)

#Definition des statistiques des armures puis des armes
class Armure:
        def __init__(self):
                self.discretion = 0
                self.defense = 0
                self.vitesse = 0
                self.magie = 0
class Plastrondecuivre(Armure):
        def __init__(self):
                self.discretion = -1
                self.defense = 3
                self.vitesse = -1
                self.magie = 0
                self.attaque = 0
                self.degat = 0
                self.image = pygame.image.load("Images/Armor-Chest.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Capedinvisibilite(Armure):
        def __init__(self):
                self.discretion = 2
                self.vitesse = 2
                self.defense = 0
                self.magie = 0
                self.degat = 0
                self.attaque = 0
                self.image = pygame.image.load("Images/Armor-Chest.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Manteaudevoleur(Armure):
        def __init__(self):
                self.discretion = 1
                self.defense = -1
                self.vitesse = 2
                self.magie = 0
                self.degat = 0
                self.attaque = 0
                self.image = pygame.image.load("Images/Armor-Chest.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Armuredeplaques(Armure):
        def __init__(self):
                self.discretion = -2
                self.defense = 4
                self.vitesse = -2
                self.magie = 0
                self.degat = 0
                self.attaque = 0
                self.image = pygame.image.load("Images/Armor-Chest.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Robedemage(Armure):
        def __init__(self):
                self.discretion = 0
                self.defense = -2
                self.vitesse = 1
                self.magie = 3
                self.degat = 0
                self.attaque = 0
                self.image = pygame.image.load("Images/Armor-Chest.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Arme:
        def __init__(self):
                self.attaque = 0
                self.vitesse = 0
                self.degat = 0
                self.magie = 0
class Epee(Arme):
        def __init__(self):
                self.attaque = 2
                self.vitesse = -1
                self.degat = 2
                self.magie = 0
                self.discretion = 0
                self.defense = 0
                self.image = pygame.image.load("Images/Sword.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Masselourde(Arme):
        def __init__(self):
                self.attaque = -2
                self.vitesse = -2
                self.degat = 4
                self.magie = 0
                self.discretion = 0
                self.defense = 0
                self.image = pygame.image.load("Images/Sword.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Dague(Arme):
        def __init__(self):
                self.attaque = 1
                self.vitesse = 2
                self.degat = 0
                self.magie = 0
                self.discretion = 0
                self.defense = 0
                self.image = pygame.image.load("Images/Sword.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Baton(Arme):
        def __init__(self):
                self.attaque = 0
                self.vitesse = 0
                self.degat = -1
                self.magie = 3
                self.discretion = 0
                self.defense = 0
                self.image = pygame.image.load("Images/Sword.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Hache(Arme):
        def __init__(self):
                self.attaque = -1
                self.vitesse = -1
                self.degat = 2
                self.magie = 0
                self.discretion = 0
                self.defense = 0
                self.image = pygame.image.load("Images/Sword.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True
class Masseapiques(Arme):
        def __init__(self):
                self.attaque = -1
                self.vitesse = -1
                self.degat = 3
                self.magie = 0
                self.discretion = 0
                self.defense = 0
                self.image = pygame.image.load("Images/Sword.png").convert_alpha()
                valide = False
                while not valide:
                    self.x = randint(6,55)
                    self.y = randint(7,48)
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    carte = carte1
                                if sprite =="2":
                                    carte = carte2
                                if sprite == "3":
                                    carte = carte3
                                if sprite == "4":
                                    carte = carte4
                                if sprite=="5":
                                    carte = carte5
                    if carte.structure[self.y][self.x]=='h':
                        valide = True

#Creation de la class generale des monstres
class Mobs:
        #Variables initiales utilisables
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
        #Fonction qui joue le role d'intelligence artificielle        
        def update(self):
                        move = 1
                        #Si le joueur est a portee, on l'attaque
                        if player.y - 1 == self.y and player.x==self.x:
                                adjacent_bas = self
                                self.attack(player)
                                move = 0
                        if player.y + 1 == self.y and player.x==self.x:
                                adjacent_haut = self
                                self.attack(player)
                                move = 0
                        if player.x - 1 == self.x and player.y==self.y:
                                adjacent_droite = self
                                self.attack(player)
                                move = 0
                        if player.x + 1 == self.x and player.y==self.y:
                                adjacent_gauche = self
                                self.attack(player)
                                move = 0
                        #Sinon si l'on attaque pas, on regarde de quel cote faut-il se deplacer
                        diffx = abs(player.x-self.x)
                        diffy = abs(player.y-self.y)
                        if diffx <= 6 and diffy <= 6 and move:
                                if randint(0,self.perception)>player.discretion:
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
                                            with open("carte.txt", "r")as fichier:
                                                for ligne in fichier:
                                                    for sprite in ligne:
                                                        if sprite =="1":
                                                            carte = carte1
                                                            mobslist = mobsN1
                                                        if sprite =="2":
                                                            carte = carte2
                                                            mobslist = mobsN2
                                                        if sprite == "3":
                                                            carte = carte3
                                                            mobslist = mobsN3
                                                        if sprite == "4":
                                                            carte = carte4
                                                            mobslist = mobsN4
                                                        if sprite=="5":
                                                            carte = carte5
                                                            mobslist = mobsN5
                                            if self.x > player.x:
                                                for mobs in mobslist:
                                                    if self.x-1 == mobs.x:
                                                        move+=1
                                                if move != 0:
                                                        self.moveleft()
                                                else:
                                                        if self.y > player.y:
                                                            self.moveup()
                                                        elif self.y < player.y:
                                                            self.movedown()
                                            elif self.x < player.x:
                                                for mobs in mobslist:
                                                    if self.x+1 == mobs.x:
                                                        move+=1
                                                if move != 0:
                                                        self.moveright()
                                                else:
                                                        if self.y > player.y:
                                                            self.moveup()
                                                        elif self.y < player.y:
                                                            self.movedown()
        #Fonctions qui permettent de se deplacer
        def moveleft(self):
                move = 0
                with open("carte.txt", "r")as fichier:
                    for ligne in fichier:
                        for sprite in ligne:
                            if sprite =="1":
                                carte = carte1
                                mobslist = mobsN1
                            if sprite =="2":
                                carte = carte2
                                mobslist = mobsN2
                            if sprite == "3":
                                carte = carte3
                                mobslist = mobsN3
                            if sprite == "4":
                                carte = carte4
                                mobslist = mobsN4
                            if sprite=="5":
                                carte = carte5
                                mobslist = mobsN5
                #On regarde si un monstre est a cote
                for mobs in mobslist:
                    if self.x-1 == mobs.x and self.y == mobs.y:
                        move+=1
                #Si la variable move est a 0, cela signifie qu'il n'y a pas de monstre de ce cote : on verifie alors s'il y a un autre obstacle
                if carte.structure[self.y][self.x-1]=='h' and move==0:
                        self.x -= 1
                    
        def moveright(self):
                move = 0
                with open("carte.txt", "r")as fichier:
                    for ligne in fichier:
                        for sprite in ligne:
                            if sprite =="1":
                                carte = carte1
                                mobslist = mobsN1
                            if sprite =="2":
                                carte = carte2
                                mobslist = mobsN2
                            if sprite == "3":
                                carte = carte3
                                mobslist = mobsN3
                            if sprite == "4":
                                carte = carte4
                                mobslist = mobsN4
                            if sprite=="5":
                                carte = carte5
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
                                carte = carte1
                                mobslist = mobsN1
                            if sprite =="2":
                                carte = carte2
                                mobslist = mobsN2
                            if sprite == "3":
                                carte = carte3
                                mobslist = mobsN3
                            if sprite == "4":
                                carte = carte4
                                mobslist = mobsN4
                            if sprite=="5":
                                carte = carte5
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
                                carte = carte1
                                mobslist = mobsN1
                            if sprite =="2":
                                carte = carte2
                                mobslist = mobsN2
                            if sprite == "3":
                                carte = carte3
                                mobslist = mobsN3
                            if sprite == "4":
                                carte = carte4
                                mobslist = mobsN4
                            if sprite=="5":
                                carte = carte5
                                mobslist = mobsN5
                for mobs in mobslist:
                    if self.x == mobs.x and self.y+1 == mobs.y:
                        move+=1
                if carte.structure[self.y+1][self.x]=='h' and move==0:
                        self.y += 1
                        
        #Fonction semblable a celle du joueur, qui calcule les degats subis
        def blesse(self,name):
                if randint(1,10)<name.attaque:
                        if randint(1,50)>self.vitesse:
                                self.valeur = randint(1,name.degat)-randint(1,self.defense)
                                if self.valeur > 0:
                                        self.pv -= self.valeur
                                        rendu_valeur = font.render(str(-self.valeur),1,(51,0,0))
                                        with open("carte.txt", "r")as fichier:
                                            for ligne in fichier:
                                                for sprite in ligne:
                                                    if sprite =="1":
                                                        mobslist = mobsN1
                                                        niveau=1
                                                    if sprite =="2":
                                                        mobslist = mobsN2
                                                        niveau=2
                                                    if sprite == "3":
                                                        mobslist = mobsN3
                                                        niveau=3
                                                    if sprite == "4":
                                                        mobslist = mobsN4
                                                        niveau=4
                                                    if sprite=="5":
                                                        mobslist = mobsN5
                                                        niveau=5
                                        for i in range(0,100):
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
                                            niveau=1
                                        if sprite =="2":
                                            mobslist = mobsN2
                                            niveau=2
                                        if sprite == "3":
                                            mobslist = mobsN3
                                            niveau=3
                                        if sprite == "4":
                                            mobslist = mobsN4
                                            niveau=4
                                        if sprite=="5":
                                            mobslist = mobsN5
                                            niveau=5
                            for i in range(0,100):
                                fenetre.blit(player.image,(640,360))
                                for mobs in mobslist:
                                    if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                        fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                        rendu_esquive = font.render("Esquive!",1,(255,0,0))
                                        fenetre.blit(rendu_esquive,(660+(self.x-player.x)*72,320+(self.y-player.y)*72))
                                for armure in stufflist:
                                                if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                                                    fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                                for arme in stufflist:
                                    if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                                        fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
                                pygame.display.flip()
                else:
                    with open("carte.txt", "r")as fichier:
                        for ligne in fichier:
                            for sprite in ligne:
                                if sprite =="1":
                                    mobslist = mobsN1
                                    niveau=1
                                if sprite =="2":
                                    mobslist = mobsN2
                                    niveau=2
                                if sprite == "3":
                                    mobslist = mobsN3
                                    niveau=3
                                if sprite == "4":
                                    mobslist = mobsN4
                                    niveau=4
                                if sprite=="5":
                                    mobslist = mobsN5
                                    niveau=5
                    for i in range(0,100):
                        fenetre.blit(player.image,(640,360))
                        for mobs in mobslist:
                            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                                    fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
                                    rendu_echec = font.render("Echec!",1,(255,0,0))
                                    fenetre.blit(rendu_echec,(670,320))
                        for armure in stufflist:
                            if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                                fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                        for arme in stufflist:
                            if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                                fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
                        pygame.display.flip()
                        
                if self.pv <= 0:
                    player.xp += self.xp
                    if niveau == 1:
                        mobsN1.remove(self)
                    if niveau == 2:
                        mobsN2.remove(self)
                    if niveau == 3:
                        mobsN3.remove(self)
                    if niveau == 4:
                        mobsN4.remove(self)
                    if niveau == 5:
                        mobsN5.remove(self)
                    del(self)

        def attack(self,name):
                name.blesse(self)

#Definitions de tous les monstres existants, avec heritage des fonctions de la class Mobs
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

#Class des sorts, avec leur duree, leur temps de rechargement etc  
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
                self.affichage="Disponible"
        class Berserk:
                def __init__(self):
                        self.duree = 7 + int(0.2*player.magie)
                        self.recharge = 20 - int(0.5*player.magie)
                        self.actif = 0
                        self.dispo = 1
                        self.affichage="Disponible"
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                def update(self):
                        if self.actif==1:
                                self.tempsecoule += 1
                                print "a"
                        if self.tempsrecharge >= self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                                self.affichage="Disponible"
                                print "b"
                        if self.tempsecoule >= self.duree:
                                player.attaque -= 2
                                player.vitesse -= 2
                                player.degat -= 1
                                self.actif = 0
                                self.affichage="Indisponible"
                                self.tempsrecharge += 1
                                print "c"
                def lancer(self):
                        if self.dispo==1:
                                player.attaque +=2
                                player.vitesse += 2
                                player.degat += 1
                                self.dispo = 0
                                self.actif = 1
                                self.affichage="En utilisation"
                                print"d"
                    
        class Corps_Dacier:
                def __init__(self):
                        self.duree = 7 + int(0.2*player.magie)
                        self.recharge = 20 - int(0.5*player.magie)
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                        self.affichage="Disponible"
                def update(self):
                        if self.actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge >= self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                                self.affichage="Disponible"
                        if self.tempsecoule >= self.duree:
                                player.defense -= 4
                                self.actif = 0
                                self.tempsrecharge += 1
                                self.affichage="Indisponible"
                def lancer(self):
                        if self.dispo:
                                player.defense += 4
                                self.dispo = 0
                                self.actif = 1
                                self.affichage="En utilisation"
                                
        class Arme_Enflammee:
                def __init__(self):
                        self.duree = 7 + int(0.2*player.magie)
                        self.recharge = 20 - int(0.5*player.magie)
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                        self.affichage="Disponible"
                def update(self):
                        if self.actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge >= self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                                self.affichage="Disponible"
                        if self.tempsecoule >= self.duree:
                                player.attaque -= 4
                                player.degat -= 1
                                self.actif = 0
                                self.tempsrecharge += 1
                                self.affichage="Indisponible"
                def lancer(self):
                        if self.dispo:
                                player.attaque +=4
                                player.degat += 1
                                self.dispo = 0
                                self.actif = 1
                                self.affichage="En utilisation"
                                
        class Invisibilite:
                def __init__(self):
                        self.duree = 7 + int(0.2*player.magie)
                        self.recharge = 20 - int(0.5*player.magie)
                        self.actif = 0
                        self.dispo = 1
                        self.tempsecoule = 0
                        self.tempsrecharge = 0
                        self.affichage="Disponible"
                def update(self):
                        if self.actif:
                                self.tempsecoule += 1
                        if self.tempsrecharge >= self.recharge:
                                self.tempsecoule = 0
                                self.dispo = 1
                                self.affichage="Disponible"
                        if self.tempsecoule >= self.duree:
                                player.discretion -= 30
                                self.actif = 0
                                self.tempsrecharge += 1
                                self.affichage="Indisponible"
                def lancer(self):
                        if self.dispo:
                                player.discretion += 30
                                self.dispo = 0
                                self.actif = 1
                                self.affichage="En utilisation"
                                
        class Soin:
                def __init__(self):
                        self.recharge = 50 - player.magie
                        self.dispo = 1
                        self.tempsrecharge = 0
                        self.affichage="Disponible"
                def update(self):
                        if not self.dispo:
                                self.tempsrecharge += 1
                        if self.tempsrecharge == self.recharge:
                                self.dispo = 1
                                self.tempsrecharge = 0
                                self.affichage="Indisponible"
                def lancer(self):
                        if self.dispo:
                                player.pv = player.pvmax
                                self.dispo = 0
                                self.affichage="Disponible"    
                                
#Instanciation de toutes les entites                             
player = Player()                       
spell = Spell()
spellslist = []
berserk = spell.Berserk()
corps_dacier = spell.Corps_Dacier()
arme_enflammee = spell.Arme_Enflammee()
invisibilite = spell.Invisibilite()
soin = spell.Soin()

#Ajout dans une liste
spellslist.extend((berserk,corps_dacier,arme_enflammee,invisibilite,soin))

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

armure = Armure()
arme = Arme()
carte1.generer()
epee = Epee()
masselourde = Masselourde()
dague = Dague()
baton = Baton()
hache = Hache()
masseapiques = Masseapiques()
plastrondecuivre = Plastrondecuivre()
capedinvisiblite = Capedinvisibilite()
manteaudevoleur = Manteaudevoleur()
armuredeplaques = Armuredeplaques()
robedemage = Robedemage()
stufflist = []
stufflist.extend((epee,masselourde,dague,baton,hache,masseapiques,plastrondecuivre,capedinvisiblite,manteaudevoleur,armuredeplaques,robedemage))

def stuffinst():
        stufflist = []
        epee = Epee()
        masselourde = Masselourde()
        dague = Dague()
        baton = Baton()
        hache = Hache()
        masseapiques = Masseapiques()
        plastrondecuivre = Plastrondecuivre()
        capedinvisiblite = Capedinvisibilite()
        manteaudevoleur = Manteaudevoleur()
        armuredeplaques = Armuredeplaques()
        robedemage = Robedemage()
        stufflist.extend((epee,masselourde,dague,baton,hache,masseapiques,plastrondecuivre,capedinvisiblite,manteaudevoleur,armuredeplaques,robedemage))
    
#Definitions des mises a jour

def spellsupdate():
    for spell in spellslist:
        spell.update()

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
                    carte1.afficher(fenetre)
                    Niveau = 1
                if sprite =="2":
                    carte2.afficher(fenetre)
                    Niveau = 2
                if sprite == "3":
                    carte3.afficher(fenetre)
                    Niveau = 3
                if sprite == "4":
                    carte4.afficher(fenetre)
                    Niveau = 4
                if sprite=="5":
                    carte5.afficher(fenetre)
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
        dispo_be = font.render(str(berserk.affichage),1,(172,35,220))
        fenetre.blit(dispo_be,(100,340))
        ecrit_ca = font.render ("Corps d'acier-touche 2",1,(255,0,0))
        fenetre.blit(ecrit_ca,(0,410))
        dispo_ca = font.render(str(corps_dacier.affichage),1,(172,35,220))
        fenetre.blit(dispo_ca,(100,440))
        ecrit_aa = font.render ("Arme d'acier-touche 3",1,(255,0,0))
        fenetre.blit(ecrit_aa,(0,510))
        dispo_aa = font.render(str(arme_enflammee.affichage),1,(172,35,220))
        fenetre.blit(dispo_aa,(100,540))
        ecrit_in = font.render ("Invisibilite-touche 4",1,(255,0,0))
        fenetre.blit(ecrit_in,(30,610))
        dispo_in = font.render(str(invisibilite.affichage),1,(172,35,220))
        fenetre.blit(dispo_in,(100,640))
        ecrit_soin = font.render ("Soin-touche 5",1,(255,0,0))
        fenetre.blit(ecrit_soin,(70,710))
        dispo_soin = font.render(str(soin.affichage),1,(172,35,220))
        fenetre.blit(dispo_soin,(100,740))
