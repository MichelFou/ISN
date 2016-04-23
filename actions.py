# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
from random import *
from bibliotheque import *
from Class import *
#definition des differentes actions possibles
nombre_de_tour_score = 0

#incrementer le nombre de tour joués
def tour_plus_un ():
    nombre_de_tour_score = nombre_de_tour_score + 1


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
        gauche= pygame.image.load("Images/Fence - side-left.png").convert_alpha()
        droite= pygame.image.load("Images/Fence - side-right.png").convert_alpha()
        milieu= pygame.image.load("Images/Fence - front-middle.png").convert_alpha()
        coin_gauche= pygame.image.load("Images/Fence - front-left.png").convert_alpha()
        coin_droite= pygame.image.load("Images/Fence - front-right.png").convert_alpha()
        tree = pygame.image.load("Images/tree.png").convert_alpha()
        herbe = pygame.image.load("Images/grass.png").convert_alpha()
        #end = pygame.image.load(image_end).convert_alpha()
        rien = pygame.image.load("Images/rien.png").convert_alpha()
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
                            fenetre.blit(end,(x,y))
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
