# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
#from actions import *
from bibliotheque import *
 
pygame.init()
font = pygame.font.SysFont("Chiller", 40)
font2 = pygame.font.SysFont("Chiller", 70)
font3 = pygame.font.SysFont("Chiller",48)
fenetre = pygame.display.set_mode((1024,768))
 
fond = pygame.image.load("fond.jpg").convert()
fenetre.blit(fond,(0,0))
k=20
pygame.display.update()
pygame.display.set_caption("Trapped!")
 
menu = 1
choix = 4
while menu:
    rendu_jouer = font3.render("Jouer",1,(255,255,255))
    jouerRect = fenetre.blit(rendu_jouer,(797,466))
    rendu_instructions = font3.render("Instructions",1,(255,255,255))
    instructionsRect = fenetre.blit(rendu_instructions,(799,538))
    rendu_credits = font3.render("Crédits",1,(255,255,255))
    creditsRect = fenetre.blit(rendu_credits,(799,617))
    rendu_quitter = font3.render("Quitter",1,(255,255,255))
    quitterRect = fenetre.blit(rendu_quitter,(799,696))
    rendu_titre = font3.render("Trapped!",1,(255,0,0))
    fenetre.blit(rendu_titre,(100,77))
    pygame.display.update()
    if choix == 4:
        for  event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                pos = pygame.mouse.get_pos()
                if jouerRect.collidepoint(pos):
                    choix = 1 # Jouer
                if instructionsRect.collidepoint(pos):
                    choix = 2 # Instructions
                if creditsRect.collidepoint(pos):
                    choix = 3 # Credits
                if quitterRect.collidepoint(pos) or event.type == QUIT:
                    pygame.quit() # Quitter
                    exit()
 
    if choix == 2:
        fond = pygame.image.load("Fond.jpg").convert()
        fenetre.blit (fond,(0,0))
        pygame.display.update()
        while choix==2:
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
            retourRect = fenetre.blit(rendu_retour,(910,711))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    choix = 0 # Retour
                if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                    pos = pygame.mouse.get_pos()
                    if retourRect.collidepoint(pos):
                        choix = 0 # Retour
    if choix == 3:
        fond = pygame.image.load("fond.jpg").convert()
        fenetre.blit(fond,(0,0))
        pygame.display.update()
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
            retourRect = fenetre.blit(rendu_retour,(910,711))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    choix = 0
                if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                    pos = pygame.mouse.get_pos()
                    if retourRect.collidepoint(pos):
                        choix = 0 # Retour
    if choix == 0:
        fenetre = pygame.display.set_mode((1024,768))
        fond = pygame.image.load("fond.jpg").convert()
        fenetre.blit (fond,(0,0))
        pygame.display.update()
        choix = 4
    if choix == 1:
        while k>=0:
            pygame.time.Clock().tick(30)
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
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<250 and event.pos[1]>214 and k>0:
                        attaque=attaque + 1
                        k=k-1
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<250 and event.pos[1]>214 and attaque>1:
                        attaque=attaque-1
                        k=k+1
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<346 and event.pos[1]>310 and k>0:    
                        defense=defense+1
                        k=k-1
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<346 and event.pos[1]>310 and defense>1:    
                        defense=defense-1
                        k=k+1
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<440 and event.pos[1]>400 and k>0:
                        vitesse=vitesse+1
                        k=k-1
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<440 and event.pos[1]>400 and vitesse>1:
                        vitesse=vitesse-1
                        k=k+1
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<550 and event.pos[1]>510 and k>0:
                        degat=degat+1
                        k=k-1
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<550 and event.pos[1]>510 and degat>1:
                        degat=degat-1
                        k=k+1
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<650 and event.pos[1]>610 and k>0:
                        discretion=discretion+1
                        k=k-1
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<650 and event.pos[1]>610 and discretion>1:
                        discretion=discretion-1
                        k=k+1
                    if event.pos[0]>560  and event.pos[0]<600 and event.pos[1]<750 and event.pos[1]>710 and k>0:    
                        magie=magie+1
                        k=k-1
                    if event.pos[0]>393  and event.pos[0]<433 and event.pos[1]<750 and event.pos[1]>710 and magie>1:    
                        magie=magie-1
                        k=k+1
            if k==0:
                ok = font2.render("Continuer", 1, (255,0,0))
                fenetre.blit(ok, (800, 670))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if event.pos[0]>800  and event.pos[0]<1000 and event.pos[1]<740 and event.pos[1]>670:
                            menu=0
                            suite=1
                           
while suite==1:
    carte= Niveau("N1.txt")
    carte.generer()
    carte.afficher(fenetre)
    pygame.display.flip()
