# -*- coding: cp1252 -*-
import pygame
from pygame.locals import*
from actions import*
from bibliotheque import*
#initialisation pygame
pygame.init()

#mise en place d'une icone et d'un titre a la fenetre
icone=pygame.image.load("Hero-right.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Trapped!")

#initialisation des polices d'ecriture
font = pygame.font.SysFont("Chiller", 40)
font2 = pygame.font.SysFont("Chiller", 70)
font3 = pygame.font.SysFont("Chiller",48)

#mise en place de la fenetre
fenetre = pygame.display.set_mode((1083,812),RESIZABLE)
fond = pygame.image.load("FOND.jpg").convert()
fenetre.blit(fond,(0,0))
pygame.display.flip()

menu = 1
choix = 4
#pygame.mixer.music.load("01-Aqualung.wav")
#pygame.mixer.music.play(-1)
while menu:
    if choix == 4:
        #écriture du texte du menu
        rendu_jouer = font3.render("Jouer",1,(255,255,255))
        fenetre.blit(rendu_jouer,(797,466))
        rendu_instructions = font3.render("Instructions",1,(255,255,255))
        fenetre.blit(rendu_instructions,(799,538))
        rendu_credits = font3.render("Crédits",1,(255,255,255))
        fenetre.blit(rendu_credits,(799,617))
        rendu_quitter = font3.render("Quitter",1,(255,255,255))
        fenetre.blit(rendu_quitter,(799,696))
        rendu_titre = font3.render("Trapped!",1,(255,0,0))
        fenetre.blit(rendu_titre,(100,77))
        pygame.display.flip()
        for  event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>794 and event.pos[0]<910 and event.pos[1]<524 and event.pos[1]>465 :
                choix = 1 # Jouer
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>794 and event.pos[0]<1024 and event.pos[1]<597 and event.pos[1]>562 :
                choix = 2 # Instructions
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>794 and event.pos[0]<940 and event.pos[1]<675 and event.pos[1]>615 :
                choix = 3 # Credits
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>794 and event.pos[0]<940 and event.pos[1]<745 and event.pos[1]>695 or event.type == QUIT:
                pygame.quit() # Quitter
                exit()

    if choix == 2:
        #fenetre d'instruction
        fond = pygame.image.load("FOND.jpg").convert()
        fenetre.blit (fond,(0,0))
        pygame.display.flip()
        while choix==2:
            #écriture du texte du menu
            pygame.time.Clock().tick(30)
            rendu_inst1 = font.render("Le but du jeu est de s'enfuir du château à",1,(255,0,0))
            fenetre.blit(rendu_inst1,(35,79))
            rendu_inst2 = font.render("à l'aide des flèches directionnelles.",1,(255,0,0))
            fenetre.blit(rendu_inst2,(35,139))
            rendu_inst3 = font.render("La barre espace permet de sauter son",1,(255,0,0))
            fenetre.blit(rendu_inst3,(35,199))
            rendu_inst4 = font.render("tour",1,(255,0,0))
            fenetre.blit(rendu_inst4,(35,259))
            rendu_inst5 = font.render("Les touches 1, 2, 3, 4 et 5, situées",1,(255,0,0))
            fenetre.blit(rendu_inst5,(35,319))
            rendu_inst6 = font.render("en haut du clavier permettent",1,(255,0,0))
            fenetre.blit(rendu_inst6,(35,379))
            rendu_inst7 = font.render("de lancer les sorts correspondants.",1,(255,0,0))
            fenetre.blit(rendu_inst7,(35,439))
            rendu_instructions_titre = font.render("Instructions",1,(255,255,255))
            fenetre.blit(rendu_instructions_titre,(870,5))
            rendu_retour = font.render("Retour",1,(255,255,255))
            fenetre.blit(rendu_retour,(910,711))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    choix = 0 #retour au menu par clavier
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>910 and event.pos[0]<1006 and event.pos[1]<740 and event.pos[1]>711 :
                    choix = 0 #retour au menu par clic
    #ecran credits
    if choix == 3:
        fond = pygame.image.load("FOND.jpg").convert()
        fenetre.blit(fond,(0,0))
        pygame.display.flip()
        #écriture du texte du menu
        while choix == 3:
            pygame.time.Clock().tick(30)
            rendu_credits1 = font.render("Programmation : GORIA Léonard",1,(255,0,0))
            fenetre.blit(rendu_credits1,(35,79))
            rendu_credits2 = font.render("BERKI Rayan",1,(255,0,0))
            fenetre.blit(rendu_credits2,(230,125))
            rendu_credits3 = font.render("Graphismes & Musiques : TAING Alexandre",1,(255,0,0))
            fenetre.blit(rendu_credits3,(35,200))
            rendu_credits_titre = font.render("Crédits",1,(255,255,255))
            fenetre.blit(rendu_credits_titre,(920,5))
            rendu_retour = font.render("Retour",1,(255,255,255))
            fenetre.blit(rendu_retour,(910,711))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    choix = 0 #retour au menu par clavier
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>910 and event.pos[0]<1006 and event.pos[1]<740 and event.pos[1]>711 :
                    choix = 0 #retour au menu par clic
#re-mise en place de la fenetre de menu dans une autre boucle pour eviter clignotement
    if choix == 0:
        fond = pygame.image.load("FOND.jpg").convert()
        fenetre.blit (fond,(0,0))
        pygame.display.flip()
        #retour a la boucle des choix
        choix = 4
    if choix == 1:
        #actualiser l'affichage tant qu'il reste des points atribuables
        while k>=0:
            pygame.time.Clock().tick(30)
            #affichage de l'ecran des competences
            skill = pygame.image.load("Skill.jpg").convert()
            fenetre.blit(skill,(0,0))
            rendu_k = font.render(str(k), 1, (255,0,0))
            fenetre.blit(rendu_k, (123, 670))
            rendu_attaque = font.render(str(attaque), 1, (255,0,0))
            fenetre.blit(rendu_attaque, (500, 214))
            rendu_defense = font.render(str(defense), 1, (255,0,0))
            fenetre.blit(rendu_defense, (500, 310))
            rendu_vitesse = font.render(str(vitesse), 1, (255,0,0))
            fenetre.blit(rendu_vitesse, (500, 400))
            rendu_degat = font.render(str(degat), 1, (255,0,0))
            fenetre.blit(rendu_degat, (500, 510))
            rendu_discretion = font.render(str(discretion), 1, (255,0,0))
            fenetre.blit(rendu_discretion, (500, 610))
            rendu_magie = font.render(str(magie), 1, (255,0,0))
            fenetre.blit(rendu_magie, (500, 710))
            pygame.display.flip()
            #si clic croix, alors quitter
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                #changement des variable pour chaque attribution de competence
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    #attaque + 
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<250 and event.pos[1]>214 and k>0:
                        attaque=attaque + 1
                        k=k-1
                    #attaque -
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<250 and event.pos[1]>214 and attaque>1:
                        attaque=attaque-1
                        k=k+1
                    #defense +
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<346 and event.pos[1]>310 and k>0:    
                        defense=defense+1
                        k=k-1
                    #defense -
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<346 and event.pos[1]>310 and defense>1:    
                        defense=defense-1
                        k=k+1
                    #vitesse +
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<440 and event.pos[1]>400 and k>0:
                        vitesse=vitesse+1
                        k=k-1
                    #vitesse -
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<440 and event.pos[1]>400 and vitesse>1:
                        vitesse=vitesse-1
                        k=k+1
                    #degat +
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<550 and event.pos[1]>510 and k>0:
                        degat=degat+1
                        k=k-1
                    #degat -
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<550 and event.pos[1]>510 and degat>1:
                        degat=degat-1
                        k=k+1
                    #discretion +
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<650 and event.pos[1]>610 and k>0:
                        discretion=discretion+1
                        k=k-1
                    #discretion -
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<650 and event.pos[1]>610 and discretion>1:
                        discretion=discretion-1
                        k=k+1
                    #magie +
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<750 and event.pos[1]>710 and k>0:    
                        magie=magie+1
                        k=k-1
                    #magie -
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<750 and event.pos[1]>710 and magie>1:    
                        magie=magie-1
                        k=k+1
            #affichage de continuer quand il n'y a plus de points atribuables
            if k==0:
                ok = font2.render("Continuer", 1, (255,0,0))
                fenetre.blit(ok, (800, 670))
                pygame.display.flip()
                #si clic sur continuer
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>800  and event.pos[0]<1000 and event.pos[1]<740 and event.pos[1]>670:
                    #sortie de la boucle "while k>=0"
                    k=-1
                    #sortie du menu
                    menu = 0
                    #entree dans la nouvelle boucle
                    suite = 1
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

#boucle du niveau 1
#musique du niveau
#pygame.mixer.music.load("01-Aqualung.wav")
#pygame.mixer.music.play(-1)
while suite==1:
    #mise en place du fond
    fond = pygame.image.load("Hud.jpg").convert()
    fenetre.blit(fond,(0,0))
    #ecriture des textes
    rendu_pv = font.render("PV :", 1, (255,0,0))
    fenetre.blit(rendu_pv,(100,10))
    point_vie = font.render(str(pv),1,(255,0,0))
    slash = font.render("/",1,(255,0,0))
    point_vie_max=font.render(str(pv_max),1,(255,0,0))
    fenetre.blit(point_vie,(70,70))
    fenetre.blit(point_vie_max,(160,70))
    fenetre.blit(slash,(120,70))
    ecris_niveau =font.render("Niveau",1,(255,0,0))
    niveau = font.render(str(lvl),1,(255,0,0))
    fenetre.blit(ecris_niveau,(80,130))
    fenetre.blit(niveau,(180,130))
    ecris_xp=font.render("XP :",1,(255,0,0))
    experience = font.render(str(xp), 1, (255,0,0))
    experience_demandee =font.render(str(xp_demande), 1, (255,0,0))
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
    ecrit_in = font.render ("Invisibilité-touche 4",1,(255,0,0))
    fenetre.blit(ecrit_in,(30,610))
    dispo_in = font.render(str(affichage_in),1,(172,35,220))
    fenetre.blit(dispo_in,(100,640))
    ecrit_soin = font.render ("Soin-touche 5",1,(255,0,0))
    fenetre.blit(ecrit_soin,(70,710))
    dispo_soin = font.render(str(affichage_soin),1,(172,35,220))
    fenetre.blit(dispo_soin,(100,740))
    #initialisation de la carte
    carte= Niveau("N1.txt")
    carte.generer()
    carte.afficher(fenetre)
    pygame.display.flip()

    #corps du jeu a coder

    #fin du niveau 1 si le joueur atteind l'arrivée
    if x_heros==29 and y_heros==6:
        suite = 2

#musique du niveau
pygame.mixer.music.load("01-Aqualung.wav")
pygame.mixer.music.play(-1)       
while suite ==2:
    #mise en place du fond
    fond = pygame.image.load("Hud.jpg").convert()
    fenetre.blit(fond,(0,0))
    #ecriture des textes
    rendu_pv = font.render("PV :", 1, (255,0,0))
    fenetre.blit(rendu_pv,(100,10))
    point_vie = font.render(str(pv),1,(255,0,0))
    slash = font.render("/",1,(255,0,0))
    point_vie_max=font.render(str(pv_max),1,(255,0,0))
    fenetre.blit(point_vie,(70,70))
    fenetre.blit(point_vie_max,(160,70))
    fenetre.blit(slash,(120,70))
    ecris_niveau =font.render("Niveau",1,(255,0,0))
    niveau = font.render(str(lvl),1,(255,0,0))
    fenetre.blit(ecris_niveau,(80,130))
    fenetre.blit(niveau,(180,130))
    ecris_xp=font.render("XP :",1,(255,0,0))
    experience = font.render(str(xp), 1, (255,0,0))
    experience_demandee =font.render(str(xp_demande), 1, (255,0,0))
    fenetre.blit(ecris_xp,(100,180))
    fenetre.blit(experience,(70,230))
    fenetre.blit(experience_demandee,(160,230))
    fenetre.blit(slash,(120,230))
    ecrit_be= font.render ("Berserk-touche 1",1,(255,0,0))
    fenetre.blit(ecrit_be,(30,310))
    dispo_be = font.render(str(affichage_be),1,(172
                                                ,35,220))
    fenetre.blit(dispo_be,(100,340))
    ecrit_ca = font.render ("Corps d'acier-touche 2",1,(255,0,0))
    fenetre.blit(ecrit_ca,(0,410))
    dispo_ca = font.render(str(affichage_ca),1,(172,35,220))
    fenetre.blit(dispo_ca,(100,440))
    ecrit_aa = font.render ("Arme d'acier-touche 3",1,(255,0,0))
    fenetre.blit(ecrit_aa,(0,510))
    dispo_aa = font.render(str(affichage_aa),1,(172,35,220))
    fenetre.blit(dispo_aa,(100,540))
    ecrit_in = font.render ("Invisibilité-touche 4",1,(255,0,0))
    fenetre.blit(ecrit_in,(30,610))
    dispo_in = font.render(str(affichage_in),1,(172,35,220))
    fenetre.blit(dispo_in,(100,640))
    ecrit_soin = font.render ("Soin-touche 5",1,(255,0,0))
    fenetre.blit(ecrit_soin,(70,710))
    dispo_soin = font.render(str(affichage_soin),1,(172,35,220))
    fenetre.blit(dispo_soin,(100,740))
    #initialisation de la carte
    carte= Niveau("N2.txt")
    carte.generer()
    carte.afficher(fenetre)
    pygame.display.flip()


    #corps du jeu à coder

    #fin du niveau 2 si le joueur atteind l'arrivée
    if x_heros==5 and y_heros==24:
        suite = 3

#musique du niveau
pygame.mixer.music.load("01-Aqualung.wav")
pygame.mixer.music.play(-1)
while suite == 3:
    #mise en place du fond
    fond = pygame.image.load("Hud.jpg").convert()
    fenetre.blit(fond,(0,0))
    #ecriture des textes
    rendu_pv = font.render("PV :", 1, (255,0,0))
    fenetre.blit(rendu_pv,(100,10))
    point_vie = font.render(str(pv),1,(255,0,0))
    slash = font.render("/",1,(255,0,0))
    point_vie_max=font.render(str(pv_max),1,(255,0,0))
    fenetre.blit(point_vie,(70,70))
    fenetre.blit(point_vie_max,(160,70))
    fenetre.blit(slash,(120,70))
    ecris_niveau =font.render("Niveau",1,(255,0,0))
    niveau = font.render(str(lvl),1,(255,0,0))
    fenetre.blit(ecris_niveau,(80,130))
    fenetre.blit(niveau,(180,130))
    ecris_xp=font.render("XP :",1,(255,0,0))
    experience = font.render(str(xp), 1, (255,0,0))
    experience_demandee =font.render(str(xp_demande), 1, (255,0,0))
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
    ecrit_in = font.render ("Invisibilité-touche 4",1,(255,0,0))
    fenetre.blit(ecrit_in,(30,610))
    dispo_in = font.render(str(affichage_in),1,(172,35,220))
    fenetre.blit(dispo_in,(100,640))
    ecrit_soin = font.render ("Soin-touche 5",1,(255,0,0))
    fenetre.blit(ecrit_soin,(70,710))
    dispo_soin = font.render(str(affichage_soin),1,(172,35,220))
    fenetre.blit(dispo_soin,(100,740))
    #initialisation de la carte
    carte= Niveau("N3.txt")
    carte.generer()
    carte.afficher(fenetre)
    pygame.display.flip()


    #corps du jeu à coder

    #fin du niveau 2 si le joueur atteind l'arrivée
    if x_heros==52 and y_heros==47:
        suite = 4

#musique du niveau
pygame.mixer.music.load("01-Aqualung.wav")
pygame.mixer.music.play(-1)        
while suite==4:
    #mise en place du fond
    fond = pygame.image.load("Hud.jpg").convert()
    fenetre.blit(fond,(0,0))
    #ecriture des textes
    rendu_pv = font.render("PV :", 1, (255,0,0))
    fenetre.blit(rendu_pv,(100,10))
    point_vie = font.render(str(pv),1,(255,0,0))
    slash = font.render("/",1,(255,0,0))
    point_vie_max=font.render(str(pv_max),1,(255,0,0))
    fenetre.blit(point_vie,(70,70))
    fenetre.blit(point_vie_max,(160,70))
    fenetre.blit(slash,(120,70))
    ecris_niveau =font.render("Niveau",1,(255,0,0))
    niveau = font.render(str(lvl),1,(255,0,0))
    fenetre.blit(ecris_niveau,(80,130))
    fenetre.blit(niveau,(180,130))
    ecris_xp=font.render("XP :",1,(255,0,0))
    experience = font.render(str(xp), 1, (255,0,0))
    experience_demandee =font.render(str(xp_demande), 1, (255,0,0))
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
    ecrit_in = font.render ("Invisibilité-touche 4",1,(255,0,0))
    fenetre.blit(ecrit_in,(30,610))
    dispo_in = font.render(str(affichage_in),1,(172,35,220))
    fenetre.blit(dispo_in,(100,640))
    ecrit_soin = font.render ("Soin-touche 5",1,(255,0,0))
    fenetre.blit(ecrit_soin,(70,710))
    dispo_soin = font.render(str(affichage_soin),1,(172,35,220))
    fenetre.blit(dispo_soin,(100,740))
    #initialisation de la carte
    carte= Niveau("N4.txt")
    carte.generer()
    carte.afficher(fenetre)
    pygame.display.flip()


    #corps du jeu à coder

    #fin du niveau 2 si le joueur atteind l'arrivée
    if x_heros==29 and y_heros==6:
        suite = 5

#musique du niveau
pygame.mixer.music.load("01-Aqualung.wav")
pygame.mixer.music.play(-1)        
while suite == 5:
    #mise en place du fond
    fond = pygame.image.load("Hud.jpg").convert()
    fenetre.blit(fond,(0,0))
    #ecriture des textes
    rendu_pv = font.render("PV :", 1, (255,0,0))
    fenetre.blit(rendu_pv,(100,10))
    point_vie = font.render(str(pv),1,(255,0,0))
    slash = font.render("/",1,(255,0,0))
    point_vie_max=font.render(str(pv_max),1,(255,0,0))
    fenetre.blit(point_vie,(70,70))
    fenetre.blit(point_vie_max,(160,70))
    fenetre.blit(slash,(120,70))
    ecris_niveau =font.render("Niveau",1,(255,0,0))
    niveau = font.render(str(lvl),1,(255,0,0))
    fenetre.blit(ecris_niveau,(80,130))
    fenetre.blit(niveau,(180,130))
    ecris_xp=font.render("XP :",1,(255,0,0))
    experience = font.render(str(xp), 1, (255,0,0))
    experience_demandee =font.render(str(xp_demande), 1, (255,0,0))
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
    ecrit_in = font.render ("Invisibilité-touche 4",1,(255,0,0))
    fenetre.blit(ecrit_in,(30,610))
    dispo_in = font.render(str(affichage_in),1,(172,35,220))
    fenetre.blit(dispo_in,(100,640))
    ecrit_soin = font.render ("Soin-touche 5",1,(255,0,0))
    fenetre.blit(ecrit_soin,(70,710))
    dispo_soin = font.render(str(affichage_soin),1,(172,35,220))
    fenetre.blit(dispo_soin,(100,740))
    #initialisation de la carte
    carte= Niveau("N5.txt")
    carte.generer()
    carte.afficher(fenetre)
    pygame.display.flip()


    #corps du jeu à coder

    #fin du niveau 2 si le joueur atteind l'arrivée
    if x_heros==29 and y_heros==12: #and persephon mort:
        suite = 6

    

               
        

