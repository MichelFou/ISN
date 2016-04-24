# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
from actions import *
from Class import *
from bibliotheque import *
#initialisation pygame
pygame.init()

#mise en place d'une icone et d'un titre a la fenetre
icone=pygame.image.load("Images/Hero-right.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Trapped!")

while 1:
    #mise en place de la fenetre
    fenetre = pygame.display.set_mode((1083,812))
    fond = pygame.image.load("Images/FOND.jpg").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    menu = 1
    gameover=0
    choix = 4
    pygame.mixer.music.load("Musiques/Musique menu.wav")
    pygame.mixer.music.play(-1)
    while menu:
        if choix == 4:
            #ecriture du texte du menu
            rendu_jouer = font3.render("Jouer",1,(255,255,255))
            fenetre.blit(rendu_jouer,(797,466))
            rendu_instructions = font3.render("Instructions",1,(255,255,255))
            fenetre.blit(rendu_instructions,(799,538))
            rendu_credits = font3.render("Credits",1,(255,255,255))
            fenetre.blit(rendu_credits,(799,617))
            rendu_quitter = font3.render("Quitter",1,(255,255,255))
            fenetre.blit(rendu_quitter,(799,696))
            rendu_titre = font3.render("Trapped!",1,(255,0,0))
            fenetre.blit(rendu_titre,(100,77))
            pygame.display.flip()
            for event in pygame.event.get():
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
            fond = pygame.image.load("Images/FOND.jpg").convert()
            fenetre.blit (fond,(0,0))
            pygame.display.flip()
            while choix==2:
                #Ã©criture du texte du menu
                pygame.time.Clock().tick(30)
                rendu_inst1 = font.render("Le but du jeu est de s'enfuir du chateau ",1,(255,0,0))
                fenetre.blit(rendu_inst1,(35,79))
                rendu_inst2 = font.render("A  l'aide des fleches directionnelles.",1,(255,0,0))
                fenetre.blit(rendu_inst2,(35,139))
                rendu_inst3 = font.render("La barre espace permet de sauter son",1,(255,0,0))
                fenetre.blit(rendu_inst3,(35,199))
                rendu_inst4 = font.render("tour",1,(255,0,0))
                fenetre.blit(rendu_inst4,(35,259))
                rendu_inst5 = font.render("Les touches 1, 2, 3, 4 et 5, situees",1,(255,0,0))
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
            fond = pygame.image.load("Images/FOND.jpg").convert()
            fenetre.blit(fond,(0,0))
            pygame.display.flip()
            #Ecriture du texte du menu
            while choix == 3:
                pygame.time.Clock().tick(30)
                rendu_credits1 = font.render("Programmation : GORIA Leonard",1,(255,0,0))
                fenetre.blit(rendu_credits1,(35,79))
                rendu_credits2 = font.render("BERKI Rayan",1,(255,0,0))
                fenetre.blit(rendu_credits2,(230,125))
                rendu_credits3 = font.render("Graphismes : TAING Alexandre",1,(255,0,0))
                fenetre.blit(rendu_credits3,(35,200))
                rendu_credits4 = font.render("Musiques : The time to run - Dexter Britain",1,(255,0,0))
                fenetre.blit(rendu_credits4,(35,275))
                rendu_credits5 = font.render("           Aydio - Deltitnu",1,(255,0,0))
                fenetre.blit(rendu_credits5,(35,325))
                rendu_credits6 = font.render("           Binaerpilot - Cornered",1,(255,0,0))
                fenetre.blit(rendu_credits6,(35,375))
                rendu_credits7 = font.render("           Mel P - Les restes de Niourk",1,(255,0,0))
                fenetre.blit(rendu_credits7,(35,425))
                rendu_credits8 = font.render("           Zero Call - A40",1,(255,0,0))
                fenetre.blit(rendu_credits8,(35,475))
                rendu_credits9 = font.render("           JT Bruce - Temporal Distortion",1,(255,0,0))
                fenetre.blit(rendu_credits9,(35,525))
                rendu_credits_titre = font.render("Credits",1,(255,255,255))
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
            fond = pygame.image.load("Images/FOND.jpg").convert()
            fenetre.blit (fond,(0,0))
            pygame.display.flip()
            #retour a la boucle des choix
            choix = 4
        if choix == 1:
            #actualiser l'affichage tant qu'il reste des points atribuables
            while k>=0:
                pygame.time.Clock().tick(30)
                #affichage de l'ecran des competences
                skill = pygame.image.load("Images/Skill.jpg").convert()
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
    update()
    #boucle du niveau 1
    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n1.wav")
    pygame.mixer.music.play(-1)
    adjacent_gauche = None
    adjacent_droite = None
    adjacent_haut = None
    adjacent_bas = None
    while suite==1:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("1")
        def_niveau.close
        carte=carte1
        carte.generer()
        carte.afficher(fenetre)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    if adjacent_gauche !=None:
                        player.attack(adjacent_gauche)
                    elif carte.structure[player.y][player.x-1]=='h':
                        player.moveleft()
                        update()
                    
                if event.key==K_UP:
                    if adjacent_haut != None:
                        player.attack(adjacent_haut)
                    elif carte.structure[player.y-1][player.x]=='h':
                        player.moveup()
                        update()

                      
                if event.key==K_DOWN:
                    if adjacent_bas != None:
                        player.attack(adjacent_bas)
                    elif carte.structure[player.y+1][player.x]=='h':
                        player.movedown()
                        update()
                      
                if event.key==K_RIGHT:
                    if adjacent_droite != None:
                        player.attack(adjacent_droite)
                    elif carte.structure[player.y][player.x+1]=='h':
                        player.moveright()
                        update()
                        
                if event.key==K_SPACE:
                    update()


                if event.key ==K_1:
                    berserk.lancer()
                    
                if event.key == K_2:
                    corps_dacier.lancer()
                    
                if event.key == K_3:
                    arme_enflammee.lancer()
                    
                if event.key== K_4:
                    invisibilite.lancer()
                    
                if event.key ==K_5:
                    soin.lancer()
                      
        if gameover == 1:
            suite = 7                

        #fin du niveau 1 si le joueur atteind l'arrivee
        if player.x==29 and player.y==6:
            suite = 2

    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n2.wav")
    pygame.mixer.music.play(-1)
    adjacent_gauche = None
    adjacent_droite = None
    adjacent_haut = None
    adjacent_bas = None
    while suite ==2:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("2")
        def_niveau.close
        carte=carte2
        carte.generer()
        carte.afficher(fenetre)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    if adjacent_gauche !=None:
                        player.attack(adjacent_gauche)
                    elif carte.structure[player.y][player.x-1]=='h':
                        player.moveleft()
                        update()
                    
                if event.key==K_UP:
                    if adjacent_haut != None:
                        player.attack(adjacent_haut)
                    elif carte.structure[player.y-1][player.x]=='h':
                        player.moveup()
                        update()

                      
                if event.key==K_DOWN:
                    if adjacent_bas != None:
                        player.attack(adjacent_bas)
                    elif carte.structure[player.y+1][player.x]=='h':
                        player.movedown()
                        update()
                      
                if event.key==K_RIGHT:
                    if adjacent_droite != None:
                        player.attack(adjacent_droite)
                    elif carte.structure[player.y][player.x+1]=='h':
                        player.moveright()
                        update()
                    
                if event.key==K_SPACE:
                    update()

                if event.key ==K_1:
                    berserk.lancer()
                    
                if event.key == K_2:
                    corps_dacier.lancer()
                    
                if event.key == K_3:
                    arme_enflammee.lancer()
                    
                if event.key== K_4:
                    invisibilite.lancer()
                    
                if event.key ==K_5:
                    soin.lancer()
                    
        if gameover == 1:
            suite = 7
            
        #fin du niveau 2 si le joueur atteind l'arrivee
        if player.x==5 and player.y==24:
            suite = 3

    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n3.wav")
    pygame.mixer.music.play(-1)
    adjacent_gauche = None
    adjacent_droite = None
    adjacent_haut = None
    adjacent_bas = None
    while suite == 3:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("3")
        def_niveau.close
        carte=carte3
        carte.generer()
        carte.afficher(fenetre)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    if adjacent_gauche !=None:
                        player.attack(adjacent_gauche)
                    elif carte.structure[player.y][player.x-1]=='h':
                        player.moveleft()
                        update()
                    
                if event.key==K_UP:
                    if adjacent_haut != None:
                        player.attack(adjacent_haut)
                    elif carte.structure[player.y-1][player.x]=='h':
                        player.moveup()
                        update()

                      
                if event.key==K_DOWN:
                    if adjacent_bas != None:
                        player.attack(adjacent_bas)
                    elif carte.structure[player.y+1][player.x]=='h':
                        player.movedown()
                        update()
                      
                if event.key==K_RIGHT:
                    if adjacent_droite != None:
                        player.attack(adjacent_droite)
                    elif carte.structure[player.y][player.x+1]=='h':
                        player.moveright()
                        update()
                    
                if event.key==K_SPACE:
                    update()

                if event.key ==K_1:
                    berserk.lancer()
                    
                if event.key == K_2:
                    corps_dacier.lancer()
                    
                if event.key == K_3:
                    arme_enflammee.lancer()
                    
                if event.key== K_4:
                    invisibilite.lancer()
                    
                if event.key ==K_5:
                    soin.lancer()
                    
        if gameover == 1:
            suite = 7                

        #fin du niveau 2 si le joueur atteind l'arrivee
        if player.x==52 and player.y==47:
            suite = 4

    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n4.wav")
    pygame.mixer.music.play(-1)
    adjacent_gauche = None
    adjacent_droite = None
    adjacent_haut = None
    adjacent_bas = None
    while suite==4:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("4")
        def_niveau.close
        carte=carte4
        carte.generer()
        carte.afficher(fenetre)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    if adjacent_gauche !=None:
                        player.attack(adjacent_gauche)
                    elif carte.structure[player.y][player.x-1]=='h':
                        player.moveleft()
                        update()
                    
                if event.key==K_UP:
                    if adjacent_haut != None:
                        player.attack(adjacent_haut)
                    elif carte.structure[player.y-1][player.x]=='h':
                        player.moveup()
                        update()

                      
                if event.key==K_DOWN:
                    if adjacent_bas != None:
                        player.attack(adjacent_bas)
                    elif carte.structure[player.y+1][player.x]=='h':
                        player.movedown()
                        update()
                      
                if event.key==K_RIGHT:
                    if adjacent_droite != None:
                        player.attack(adjacent_droite)
                    elif carte.structure[player.y][player.x+1]=='h':
                        player.moveright()
                        update()
                    
                if event.key==K_SPACE:
                    update()

                if event.key ==K_1:
                    berserk.lancer()
                    
                if event.key == K_2:
                    corps_dacier.lancer()
                    
                if event.key == K_3:
                    arme_enflammee.lancer()
                    
                if event.key== K_4:
                    invisibilite.lancer()
                    
                if event.key ==K_5:
                    soin.lancer()
                    
        if gameover == 1:
            suite = 7

        #fin du niveau 2 si le joueur atteind l'arrivee
        if player.x==29 and player.y==6:
            suite = 5

    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n5.wav")
    pygame.mixer.music.play(-1)
    adjacent_gauche = None
    adjacent_droite = None
    adjacent_haut = None
    adjacent_bas = None
    while suite == 5:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("5")
        def_niveau.close
        carte=carte5
        carte.generer()
        carte.afficher(fenetre)
        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    if adjacent_gauche !=None:
                        player.attack(adjacent_gauche)
                    elif carte.structure[player.y][player.x-1]=='h':
                        player.moveleft()
                        update()
                    
                if event.key==K_UP:
                    if adjacent_haut != None:
                        player.attack(adjacent_haut)
                    elif carte.structure[player.y-1][player.x]=='h':
                        player.moveup()
                        update()

                      
                if event.key==K_DOWN:
                    if adjacent_bas != None:
                        player.attack(adjacent_bas)
                    elif carte.structure[player.y+1][player.x]=='h':
                        player.movedown()
                        update()
                      
                if event.key==K_RIGHT:
                    if adjacent_droite != None:
                        player.attack(adjacent_droite)
                    elif carte.structure[player.y][player.x+1]=='h':
                        player.moveright()
                        update()
                    
                if event.key==K_SPACE:
                    update()

                if event.key ==K_1:
                    berserk.lancer()
                    
                if event.key == K_2:
                    corps_dacier.lancer()
                    
                if event.key == K_3:
                    arme_enflammee.lancer()
                    
                if event.key== K_4:
                    invisibilite.lancer()
                    
                if event.key ==K_5:
                    soin.lancer()
                    
        if gameover == 1:
            suite = 7                

        #fin du niveau 2 si le joueur atteind l'arrivee
        if player.x==29 and player.y==12: #and persephon mort:
            suite = 6
    while suite ==6:
        fond = pygame.image.load("Images/Gagne.jpg").convert()
        fenetre.blit(fond,(0,0))
        fenetre.blit(ok, (800, 670))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>800  and event.pos[0]<1000 and event.pos[1]<740 and event.pos[1]>670:
                menu = 1
                suite = 0
            
            
    while suite==7:
        fond = pygame.image.load("Images/Game over.jpg").convert()
        Recommencer = font2.render("Recommencer", 1, (255,0,0))
        fenetre.blit(fond,(0,0))
        fenetre.blit(Recommencer, (800, 670))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>800  and event.pos[0]<1000 and event.pos[1]<740 and event.pos[1]>670:
                menu = 1
                suite=0
            
    
    

    

               
        

