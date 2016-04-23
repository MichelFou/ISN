# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
from random import *
from bibliotheque import *
#definition des differentes actions possibles

spellslist = []
berserk = Spell.Berserk()
corps_dacier = Spell.Corps_Dacier()
arme_enflammee = Spell.Arme_Enflammee()
invisibilite = Spell.Invisibilite()
soin = Spell.Soin()

spellslist.extend((berserk,corps_dacier,arme_enflamme,invisibilite,soin))

def spellsupdate():
    for Spell in spellslist:
        Spell.update()

player = Player()


mobslist = []
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
orc1N1 = Mobs.Orc(47,18)
orc2N1 = Mobs.Orc(30,29)
orc3N1 = Mobs.Orc(14,32)
orc4N1 = Mobs.Orc(28,10)
orc5N1 = Mobs.Orc(34,13)
orc6N1 = Mobs.Orc(11,17)

def mobsupdate():
    for Mobs in mobslist:
        Mobs.update()


def update():
    mobsupdate()
    spellsupdate()
    player.update()


#incrementer le nombre de tour joués
def tour_plus_un ():
    nombre_de_tour_score = nombre_de_tour_score + 1
    nombre_de_tour_be = nombre_de_tour_be + 1
    nombre_de_tour_ca = nombre_de_tour_ca + 1
    nombre_de_tour_aa = nombre_de_tour_aa + 1
    nombre_de_tour_in = nombre_de_tour_in + 1
    nombre_de_tour_soin = nombre_de_tour_soin + 1

#affichage de la map
class Niveau:
    #initialisation
    def __init__(self,fichier):
        self.fichier = fichier
        self.structure = 0
    def generer(self):
        #ouverture du fichier dee niveau demandé
        with open(self.fichier, "r")as fichier:
            #création liste structure
            structure_niveau=[]
            #lecture dans les lignes du fichier
            for ligne in fichier:
                #création d'une liste des lignes
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
        loup = pygame.image.load(image_loup).convert_alpha()
        orc = pygame.image.load(image_orc).convert_alpha()
        gobelin = pygame.image.load(image_gobelin).convert_alpha()
        centaure = pygame.image.load(image_centaure).convert_alpha()
        knight = pygame.image.load(image_knight).convert_alpha()
        mort_vivant = pygame.image.load(image_mort_vivant).convert_alpha()
        squelette = pygame.image.load(image_squelette).convert_alpha()
        araignee = pygame.image.load(image_araignee).convert_alpha()
        persephon = pygame.image.load(image_persephon).convert_alpha()
        wall = pygame.image.load(image_wall).convert_alpha()
        tree = pygame.image.load(image_tree).convert_alpha()
        herbe = pygame.image.load(image_herbe).convert_alpha()
        joueur = pygame.image.load("Hero-up.png").convert_alpha()
        end = pygame.image.load(image_end).convert_alpha()
        rien = pygame.image.load(image_rien).convert_alpha()
        ligne_affichee = 0
        num_ligne = 0
        #on lit chaque ligne de self structure
        for ligne in self.structure:
            #si la ligne est située à 6 sur l'axe des y du heros on continue ce qui definit un champs de vision
            if num_ligne>y_heros -6 and num_ligne<y_heros+6:
                case_affichee = 0
                num_sprite = 0
                #on lit dans les sprites
                for sprite in ligne:
                    #on définit x et y en fonction de la taille des sprites
                    x=(case_affichee* taille_sprite)+280
                    y=(ligne_affichee* taille_sprite)+10
                    #si le sprite est situé a 6 sur l'axe des x on continue cela définit completemnt le champ de vision
                    if num_sprite>x_heros -6 and num_sprite<x_heros+6:
                        #on teste pour chaque sprite quelle lettre pour savoir quel ennemi ou texture afficher
                        if sprite =='l':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(loup,(x,y))
                        elif sprite =='o':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(orc,(x,y))
                        elif sprite =='g':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(gobelin,(x,y))
                        elif sprite =='s':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(squelette,(x,y))
                        elif sprite =='a':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(araignee,(x,y))
                        elif sprite =='p':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(persephon,(x,y))
                        elif sprite =='j':
                            fenetre.blit(herbe,(x,y))
                            fenetre.blit(joueur,(x,y))
                        elif sprite =='w':
                            fenetre.blit(wall,(x,y))
                        elif sprite =='h':
                            fenetre.blit(herbe,(x,y))
                        elif sprite =='t':
                            fenetre.blit(tree,(x,y))
                        elif sprite =='m':
                            fenetre.blit(mort_vivant,(x,y))
                        elif sprite =='e':
                            fenetre.blit(end,(x,y))
                        elif sprite =='k':
                            fenetre.blit(knight,(x,y))
                        elif sprite =='c':
                            fenetre.blit(centaure,(x,y))
                        elif sprite == 'r':
                            fenetre.blit(rien,(x,y))
                        #on incrémente l'endroit ou sera affiché la case
                        case_affichee = case_affichee + 1
                    #on incrémente le numero du sprite testé pour évaluer si il se trouve dans le champ de vision
                    num_sprite = num_sprite + 1
                #on incrémente la ligne ou sera affiché la case
                ligne_affichee = ligne_affichee+1
            #on incrémente la ligne testée pour évaluer si elle est dans le champ de vision
            num_ligne = num_ligne+1
