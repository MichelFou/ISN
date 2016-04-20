# -*- coding: cp1252 -*-
import pygame
# variables
x_heros = 30
y_heros = 47
k=20

#taille d'un sprite
taille_sprite = 72
#variable niveau
lvl = 1
#variable Xp pour niveau suivant
xp_demande = lvl * 50
#variable xp du joueur
xp = 0
#points de vie
pv = 60
pv_max = 60

#bibliotheque

class Perso:
    def __init__(self,droite,gauche,haut,bas,x,y,direction,lvl,xp_demande,xp,pv,pv_max,discretion,attaque,defense,vitesse,magie,degat,mort):
	self.droite = pygame.image.load("Hero-right.png")
	self.gauche = pygame.image.load("Hero-left.png")
	self.haut = pygame.image.load("Hero-back.png")
	self.bas = pygame.image.load("Hero-front.png")
	self.x = xperso
	self.y = yperso
	self.direction = self.bas
    	self.lvl = lvl
	self.xp_demande = lvl*50
    	self.xp = xp
    	self.pv = pv
    	self.pv_max = pv_max
    	self.discretion = discretion
    	self.attaque = attaque
    	self.defense = defense
    	self.vitesse = vitesse
    	self.degat = degat
    	self.magie = magie
    	fenetre.blit(self.direction,self.x,self.y)
    	self.mort = False
    def deplacer(self,direction):
    	if direction == "droite":
    	    self.xperso+=5
    	    self.direction = self.droite
    	if direction == "gauche":
    	    self.xperso-=5
    	    self.direction = self.gauche
    	if direction == "haut":
	    self.yperso-=5
	    self.direction = self.haut
	if direction == "bas":
	    self.yperso+=5
            self.direction = self.bas
    def update(self):
        if self.pv <= 0:
            self.mort = True

#competences de base

discretion= 1
attaque = 1
defense = 1
vitesse = 1
degat = 1
magie = 1



#caracteristiques armes
#caracteristique epée de fer
attaque_ef = attaque + 2
vitesse_ef = vitesse - 1
degat_ef = degat + 2

#caracteristique masse lourde
attaque_ml = attaque - 2
vitesse_ml = vitesse - 2
degat_ml = degat + 4

#caracteristique dague legere
attaque_dl = attaque + 2
vitesse_dl = vitesse + 1

#caracteristique baton de magnus
degat_bm = degat - 1
magie_bm = magie + 3

#caracteristique hache ensanglantee
attaque_he = attaque -1
vitesse_he = vitesse - 1
degat_he = degat + 3

#caracteristique masse a pique
attaque_mp = attaque - 1
discretion_mp = discretion -1
vitesse_mp = vitesse -1
degat_mp = degat + 3


#caracteristiques equipement
#caracteristique bottes de 7 lieu
defense_7l = defense - 2
vitesse_7l = vitesse + 3
magie_7l = magie + 1

#caracteristique plastron de cuivre
discretion_pc = discretion - 1
defense_pc = defense + 3
vitesse_pc = vitesse - 1

#caracteristique cape d'invisibilite
discretion_ci = discretion + 2
vitesse_ci = vitesse + 1

#caracteristique manteau de voleur
discretion_mv = discretion + 1
defense_mv = defense + 1
vitesse_mv = vitesse +2

#caracteristique armure de plaques
discretion_ap = discretion - 2
defense_ap = defense + 4
vitesse_ap = vitesse - 2

#caracteristique casque de cuir
defense_cc = defense + 1

#caracteristique casque brillant
defense_cb = defense + 2

#caracteristique casque elfique
discretion_ce = discretion + 1
defense_ce = defense + 1
vitesse_ce = vitesse + 1
degat_ce = degat - 1
magie_ce = magie + 1

#caracteristique gants de forgeron
attaque_gf = attaque + 2
defense_gf = defense + 1
vitesse_gf = vitesse - 4

#caracteristique bottes de fer
discretion_bf = discretion - 1
defense_bf = defense +3
vitesse_bf = vitesse - 1

#caracteristiques robe de mage
defense_rm = defense - 2
vitesse_rm = vitesse + 1
magie_rm = magie + 3

#caracteristiques monstres

class Loup1:
    def __init__(self,x,y,attaque,perception,defense,vitesse,degat,xp,pv):
	self.loup = pygame.image.load("loup.png").convert_alpha()
	self.y=y
	self.x=x
	self.attaque = 10
	self.perception = 20
	self.defense = 7
	self.vitesse = 17
	self.degat = 5
	self.xp = 7
	self.pv = 20
    def update(self):
        if self.pv <= 0:
            self.mort = True

#caracteristique loup
attaque_lo = 10
perception_lo = 20
defense_lo = 7
vitesse_lo = 17
degat_lo = 5
xp_lo = 7
pv_la = 20
image_loup= "persos.png"

#caracteristique orc
attaque_or = 15
perception_or = 20
defense_or = 8
vitesse_or = 15
degat_or = 8
xp_or = 8
pv_or = 20
image_orc= "persos.png"

#caracteristique gobelin
attaque_go = 18
perception_go =10
defense_go =8
vitesse_go =15
degat_go =7
xp_go =8
pv_go =20
image_gobelin="persos.png"

#caracteristique centaure
attaque_cen =20
perception_cen =17
defense_cen =10
vitesse_cen =20
degat_cen =8
xp_cen =9
pv_cen =25
image_centaure="persos.png"

#caracteristique cavalier
attaque_cav =21
perception_cav =20
defense_cav =15
vitesse_cav =20
degat_cav =9
xp_cav =12
pv_cav =25
image_knight ="persos.png"

#caracteristique mort vivant
attaque_mo =8
perception_mo =10
defense_mo =8
vitesse_mo =10
degat_mo =5
xp_mo =7
pv_mo =15
image_mort_vivant="persos.png"

#caracteristique squelette
attaque_sq =10
perception_sq =15
defense_sq =6
vitesse_sq =13
degat_sq =6
xp_sq =8
pv_sq =15
image_squelette="persos.png"

#caracteristique araignée
attaque_ar =23
perception_ar =17
defense_ar =10
vitesse_ar =17
degat_ar =8
xp_ar=10
pv_ar =20
image_araignee ="persos.png"

#caracteristique persephon
attaque_pe =21
perception_pe=30
defense_pe =15
vitesse_pe =17
degat_pe =25
xp_pe = 50
pv_pe =70
image_persephon ="persos.png"

#definition des images du décors
image_wall="herbe.png"
image_tree="herbe.png"
image_end="herbe.png"
image_rien = "rien.png"
image_herbe = "herbe.png"

#definition des images du personnage joueur
image_joueur_haut="Hero-back.png"
image_joueur_bas="Hero-front.png"
image_joueur_droite="Hero-right.png"
image_joueur_gauche="Hero-left.png"





