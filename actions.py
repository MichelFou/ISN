# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
from random import *
from bibliotheque import *
#definition des differentes actions possibles
#lancer de dé 30

def de_30 ():
    de_30= randint(1,30)

#lancer du dé de degat

def de_degat ():
    de_degat = randint(1,degat)

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

            
                

                

#definition des differents sorts
#berserk
def berserk():                         #effet du sort
    duree_be = 7 + magie
    nombre_de_tour_be = 0
    recharge_be = 20 - magie
    attaque = attaque + 2
    vitesse = vitesse + 2
    degat = degat + 1
    berserk = 0
    action_be = 1
    affichage_be="En cours"
def fin_berserk():              #arret de l'effet au bout de la fin du sort
    attaque = attaque - 2
    vitesse = vitesse -2
    degat = degat - 1
    nombre_de_tour_be = 0
    action_be=0
    affichage_be="Indisponible"
def recharge_berserk():         #retour positif du sort qui peut etre reutilisé
    berserk = 1
    affichage_be="Disponible"
    



#corps d'acier

def corps_d_acier ():
    duree_ca = 7 + magie
    nombre_de_tour_ca = 0
    recharge_ca = 30 - magie
    defense = defense + 4
    corps_d_acier = 0
    action_ca = 1
    affichage_ca="En cours"
def fin_corps_d_acier():
    defense = defense - 4
    nombre_de_tour_be = 0
    action_ce = 0
    affichage_ca="Indisponible"
def recharge_corps_d_acier():
    corps_d_acier=1
    affichage_ca="Disponible"

#arme d'acier

def arme_d_acier():
    duree_aa=7+ magie
    nombre_de_tour_aa = 0
    recharge_aa=30 - magie
    arme_d_acier = 0
    action_aa = 1
    attaque=attaque +4
    degat=degat + 1
    affichage_aa="En cours"
def fin_arme_d_acier():
    attaque = attaque - 4
    degat = degat - 1
    action_ca = 0
    nombre_de_tour_aa = 0
    affichage_aa="Indisponible"
def recharge_arme_d_acier():
    arme_d_acier = 1
    affichage_aa="Disponible"


#invisibilite

def invisibilite():
    duree_in = 10 + magie
    nombre_de_tour_in = 0
    recharge_in = 10 - magie
    invisibilite = 0
    action_in = 1
    stealth = stealth + 30
    affichage_in="En cours"
def fin_invisibilite():
    stealth = stealth - 30
    nombre_de_tour_in = 0
    action_in = 0
    affichage_in="Indisponible"
def recharge_invisibilite ():
    invisibilite = 1
    affichage_in="Disponible"
    


#soin

def soin ():
    recharge_soin = 50 - magie
    nombre_de_tour_soin = 0
    pv = pv_max
    action_soin = 1
    soin = 0
    affichage_soin="Indisponible"
def recharge_soin ():
    soin = 1
    affichage_soin="Disponible"
        
    
        
    
