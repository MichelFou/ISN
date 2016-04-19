# -*- coding: cp1252 -*-
import pygame
from pygame.locals import*
from random import *
from bibliotheque import*
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
    def __init__(self,fichier):
        self.fichier = fichier
        self.structure = 0
    def generer(self):
        with open(self.fichier, "r")as fichier:
            structure_niveau=[]
            num_sprite=0
            num_ligne=0
            for ligne in fichier:
                ligne_niveau=[]
                for sprite in ligne:
                    if num_sprite>x_heros - 6 and num_sprite<x_heros + 6:
                        ligne_niveau.append(sprite)
                    num_sprite = num_sprite+1
                if num_ligne>y_heros - 6 and num_ligne<y_heros + 6:
                    structure_niveau.append(ligne_niveau)
                num_ligne = num_ligne+1
            self.structure = structure_niveau
    def afficher(self, fenetre):
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
        joueur = pygame.image.load(image_joueur_haut).convert_alpha()
        end = pygame.image.load(image_end).convert_alpha()
        rien = pygame.image.load(image_rien).convert_alpha()
        ligne_affichee = 0
        for ligne in self.structure:
            case_affichee = 0
            for sprite in ligne:
                x=case_affichee* taille_sprite
                y=ligne_affichee* taille_sprite
                if sprite =='l':
                    fenetre.blit(loup,(x,y))
                    fenetre.blit(herbe,(x,y))
                if sprite =='o':
                    fenetre.blit(orc,(x,y))
                    fenetre.blit(herbe,(x,y))
                if sprite =='g':
                    fenetre.blit(gobelin,(x,y))
                    fenetre.blit(herbe,(x,y))
                if sprite =='s':
                    fenetre.blit(squelette,(x,y))
                    fenetre.blit(herbe,(x,y))
                if sprite =='a':
                    fenetre.blit(araignee,(x,y))
                    fenetre.blit(herbe,(x,y))
                if sprite =='p':
                    fenetre.blit(persephon,(x,y))
                    fenetre.blit(herbe,(x,y))
                if sprite =='j':
                    fenetre.blit(joueur,(x,y))
                    fenetre.blit(herbe,(x,y))
                if sprite =='w':
                    fenetre.blit(wall,(x,y))
                if sprite =='h':
                    fenetre.blit(herbe,(x,y))
                if sprite =='t':
                    fenetre.blit(tree,(x,y))
                if sprite =='m':
                    fenetre.blit(mort_vivant,(x,y))
                if sprite =='e':
                    fenetre.blit(end,(x,y))
                if sprite =='k':
                    fenetre.blit(knight,(x,y))
                if sprite =='c':
                    fenetre.blit(centaure,(x,y))
                if sprite =='r':
                    fenetre.blit(rien,(x,y))
                case_affichee = case_affichee + 1
            ligne_affichee = ligne_affichee+1
            
                
                
            
        
        
        
                

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
def fin_berserk():              #arret de l'effet au bout de la fin du sort
    attaque = attaque - 2
    vitesse = vitesse -2
    degat = degat - 1
    nombre_de_tour_be = 0
    action_be=0
def recharge_berserk():         #retour positif du sort qui peut etre reutilisé
    berserk = 1        



#corps d'acier

    def corps_d_acier ():
        duree_ca = 7 + magie
        nombre_de_tour_ca = 0
        recharge_ca = 30 - magie
        defense = defense + 4
        corps_d_acier = 0
        action_ca = 1
    def fin_corps_d_acier():
        defense = defense - 4
        nombre_de_tour_be = 0
        action_ce = 0
    def recharge_corps_d_acier():
        corps_d_acier=1

#arme d'acier

    def arme_d_acier():
        duree_aa=7+ magie
        nombre_de_tour_aa = 0
        recharge_aa=30 - magie
        arme_d_acier = 0
        action_aa = 1
        attaque=attaque +4
        degat=degat + 1
    def fin_arme_d_acier():
        attaque = attaque - 4
        degat = degat - 1
        action_ca = 0
        nombre_de_tour_aa = 0
    def recharge_arme_d_acier():
        arme_d_acier = 1


#invisibilite

    def invisibilite():
        duree_in = 10 + magie
        nombre_de_tour_in = 0
        recharge_in = 10 - magie
        invisibilite = 0
        action_in = 1
        stealth = stealth + 30
    def fin_invisibilite():
        stealth = stealth - 30
        nombre_de_tour_in = 0
        action_in = 0
    def recharge_invisibilite ():
        invisibilite = 1
    


#soin

    def soin ():
        recharge_soin = 50 - magie
        nombre_de_tour_soin = 0
        pv = pv_max
        action_soin = 1
        soin = 0
    def recharge_soin ():
        soin = 1
        
    
        
    
