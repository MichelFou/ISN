# -*- coding: cp1252 -*-
import pygame
from pygame.locals import *
from Class import *
from bibliotheque import *
#initialisation pygame
pygame.init()

#mise en place d'une icone et d'un titre a la fenetre
icone=pygame.image.load("Images/Hero-right.png")
pygame.display.set_icon(icone)
pygame.display.set_caption("Trapped!")

#Lancement de la boucle principale pour que le jeu puisse recommencer
while 1:
    #mise en place de la fenetre
    fond = pygame.image.load("Images/FOND.jpg").convert()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()
    menu = 1
    choix = 4
    #Lancement de la musique
    pygame.mixer.music.load("Musiques/Musique menu.wav")
    pygame.mixer.music.play(-1)
    #boucle du menu
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
            rendu_titre = Trapped.render("Trapped!",1,(0,0,0))
            fenetre.blit(rendu_titre,(100,77))
            pygame.display.flip()
            #Verification si il y a un clic dans une des zones du menu
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
                #Ecriture du texte du menu
                pygame.time.Clock().tick(30)
                rendu_inst1 = font.render("Le but du jeu est de s'enfuir du chateau",1,(51,0,0))
                fenetre.blit(rendu_inst1,(35,79))
                rendu_inst2 = font.render("a l'aide des fleches directionnelles.",1,(51,0,0))
                fenetre.blit(rendu_inst2,(35,139))
                rendu_inst3 = font.render("La barre espace permet de sauter son",1,(51,0,0))
                fenetre.blit(rendu_inst3,(35,199))
                rendu_inst4 = font.render("tour",1,(51,0,0))
                fenetre.blit(rendu_inst4,(35,259))
                rendu_inst5 = font.render("Les touches 1, 2, 3, 4 et 5, situees",1,(51,0,0))
                fenetre.blit(rendu_inst5,(35,319))
                rendu_inst6 = font.render("en haut du clavier permettent",1,(51,0,0))
                fenetre.blit(rendu_inst6,(35,379))
                rendu_inst7 = font.render("de lancer les sorts correspondants.",1,(51,0,0))
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
                rendu_credits1 = font.render("Programmation : GORIA Leonard",1,(51,0,0))
                fenetre.blit(rendu_credits1,(35,79))
                rendu_credits2 = font.render("BERKI Rayan",1,(51,0,0))
                fenetre.blit(rendu_credits2,(230,125))
                rendu_credits3 = font.render("Graphismes : TAING Alexandre",1,(51,0,0))
                fenetre.blit(rendu_credits3,(35,200))
                rendu_credits4 = font.render("Musiques : The time to run - Dexter Britain",1,(51,0,0))
                fenetre.blit(rendu_credits4,(35,275))
                rendu_credits5 = font.render("           Aydio - Deltitnu",1,(51,0,0))
                fenetre.blit(rendu_credits5,(35,325))
                rendu_credits6 = font.render("           Binaerpilot - Cornered",1,(51,0,0))
                fenetre.blit(rendu_credits6,(35,375))
                rendu_credits7 = font.render("           Mel P - Les restes de Niourk",1,(51,0,0))
                fenetre.blit(rendu_credits7,(35,425))
                rendu_credits8 = font.render("           Zero Call - A40",1,(51,0,0))
                fenetre.blit(rendu_credits8,(35,475))
                rendu_credits9 = font.render("           JT Bruce - Temporal Distortion",1,(51,0,0))
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
                skill = pygame.image.load("Images/skill.jpg")
                fenetre.blit(skill,(0,0))
                rendu_k = font.render(str(k), 1, (255,255,255))
                fenetre.blit(rendu_k, (123, 670))
                rendu_attaque = font.render(str(attaque), 1, (255,255,255))
                fenetre.blit(rendu_attaque, (500, 214))
                rendu_defense = font.render(str(defense), 1, (255,255,255))
                fenetre.blit(rendu_defense, (500, 310))
                rendu_vitesse = font.render(str(vitesse), 1, (255,255,255))
                fenetre.blit(rendu_vitesse, (500, 400))
                rendu_degat = font.render(str(degat), 1, (255,255,255))
                fenetre.blit(rendu_degat, (500, 510))
                rendu_discretion = font.render(str(discretion), 1, (255,255,255))
                fenetre.blit(rendu_discretion, (500, 610))
                rendu_magie = font.render(str(magie), 1, (255,255,255))
                fenetre.blit(rendu_magie, (500, 710))
                rendu_attribution = font2.render("Menu d'attribution des competences",1,(255,255,255))
                fenetre.blit(rendu_attribution,(170,60))
                rendu_ptrestants = font3.render("Points restants",1,(255,255,255))
                fenetre.blit(rendu_ptrestants,(30,600))
                rendu__attaque = font3.render("Attaque",1,(255,255,255))
                fenetre.blit(rendu__attaque,(620,214))
                rendu__defense = font3.render("Defense",1,(255,255,255))
                fenetre.blit(rendu__defense,(620,310))
                rendu__vitesse = font3.render("Vitesse",1,(255,255,255))
                fenetre.blit(rendu__vitesse,(620,410))
                rendu__force = font3.render("Force",1,(255,255,255))
                fenetre.blit(rendu__force,(620,510))
                rendu__discretion = font3.render("Discretion",1,(255,255,255))
                fenetre.blit(rendu__discretion,(620,610))
                rendu__magie = font3.render("Magie",1,(255,255,255))
                fenetre.blit(rendu__magie,(620,710))
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
                    ok = font2.render("Continuer", 1, (255,255,255))
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
    #attribution des points de competence à l'entité player 
    player.attaque = attaque+30
    player.defense = defense
    player.vitesse = vitesse
    player.degat = degat+20
    player.discretion = discretion
    player.magie = magie
    #boucle du niveau 1
    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n1.wav")
    pygame.mixer.music.play(-1)
    #placement du personnage
    player.x = 30
    player.y = 47    
    while suite==1:
        #affichage du hud
        hud()
        Niveau = 1
        #ecriture du la variable de niveau dans un document texte pour pouvoir etre recuperee dans les autres fichiers
        def_niveau = open("carte.txt", "w")
        def_niveau.write("1")
        def_niveau.close()
        #generation de la carte
        carte1.generer()
        carte1.afficher(fenetre)
        #verification si un ennemi est dans le champ de vision du joueur
        for mobs in mobsN1:
            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:  
              #affichage de celui ci
                fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
        for armure in stufflist:
            if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                if armure.x == player.x and armure.y == player.y:
                        player.equiper_armure(armure)
        for arme in stufflist:
            if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
                if arme.x == player.x and arme.y == player.y:
                        player.equiper_arme(arme)
        #affichage du personnage au centre de l'ecran
        fenetre.blit(player.image,(640,360))
        pygame.display.flip()
        #attente de pression de touches
        for event in pygame.event.get():
            jouer = 0
            #arret du programme si clic croix
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
              #si clic sur la fleche droite
                if event.key==K_LEFT:
                  #verification si il y a un ennemi proche de lui
                    for mobs in mobsN1:
                      #si il n'a pas joue il attaque
                        if jouer == 0:
                            if mobs.x==player.x-1 and mobs.y==player.y:
                                player.image = c
                                player.attack(mobs)
                                #on met a jour
                                update()
                                #le joueur a joue
                                jouer = 1
                    #si il n'y a pas de monstres proches et que la case est de l'herbe ou la fin, il avance
                    if jouer !=1:
                        if carte1.structure[player.y][player.x-1]=='h' or carte1.structure[player.y][player.x-1]=='e':
                            player.moveleft()
                            #on met a jour
                            update()
                #si clic sur la fleche haute il se passe la meme chose que plus haut
                if event.key==K_UP:
                    for mobs in mobsN1:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y-1:
                                player.image = a
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte1.structure[player.y-1][player.x]=='h' or carte1.structure[player.y-1][player.x]=='e':
                            player.moveup()
                            update()

                #si clic sur la fleche basse il se passe la meme chose que plus haut
                if event.key==K_DOWN:
                    for mobs in mobsN1:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y+1:
                                player.image = b
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte1.structure[player.y+1][player.x]=='h' or carte1.structure[player.y+1][player.x]=='e':
                            player.movedown()
                            update()
                      
                #si clic sur la fleche droite il se passe la meme chose que plus haut
                if event.key==K_RIGHT:
                    for mobs in mobsN1:
                        if jouer == 0:
                            if mobs.x==player.x+1 and mobs.y==player.y:
                                player.image = d
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte1.structure[player.y][player.x+1]=='h' or carte1.structure[player.y][player.x+1]=='e':
                            player.moveright()
                            update()
                        
                #si clic sur la barre d'espace
                if event.key==K_SPACE:
                    #on met a jour sans mouvement du personnage
                    update()

                #Si clic sur 1 lancement du sort berserk
                if event.key ==K_1:
                    berserk.lancer()
                    
                #Si clic sur 1 lancement du sort corps d'acier
                if event.key == K_2:
                    corps_dacier.lancer()
                    
                #Si clic sur 1 lancement du sort arme enflamee
                if event.key == K_3:
                    arme_enflammee.lancer()
                    
                #Si clic sur 1 lancement du sort invisibilite
                if event.key== K_4:
                    invisibilite.lancer()
                    
                #Si clic sur 1 lancement du sort soin
                if event.key ==K_5:
                    soin.lancer()

        #si le joueur est mort              
        if player.estmort == True:
            #passage a la variable qui mene a l'ecran de game over
            suite = 7                

        #fin du niveau 1 si le joueur atteind l'arrivee
        if player.x==29 and player.y==6:
            suite = 2

    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n2.wav")
    pygame.mixer.music.play(-1)
    player.x = 30
    player.y = 47
    stuffinst()
    #meme fonctionnement que le niveau 1
    while suite ==2:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("2")
        Niveau = 2
        def_niveau.close()
        carte2.generer()
        carte2.afficher(fenetre)
        for mobs in mobsN2:
            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
        for armure in stufflist:
            if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                if armure.x == player.x and armure.y == player.y:
                        player.equiper_armure(armure)
        for arme in stufflist:
            if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
                if arme.x == player.x and arme.y == player.y:
                        player.equiper_arme(arme)
        fenetre.blit(player.image,(640,360))
        pygame.display.flip()
        for event in pygame.event.get():
            jouer = 0
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    for mobs in mobsN2:
                        if jouer == 0:
                            if mobs.x==player.x-1 and mobs.y==player.y:
                                player.image = c
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte2.structure[player.y][player.x-1]=='h' or carte2.structure[player.y][player.x-1]=='e':
                            player.moveleft()
                            update()
                if event.key==K_UP:
                    for mobs in mobsN2:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y-1:
                                player.image = a
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte2.structure[player.y-1][player.x]=='h' or carte2.structure[player.y-1][player.x]=='e':
                            player.moveup()
                            update()

                      
                if event.key==K_DOWN:
                    for mobs in mobsN2:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y+1:
                                player.image = b
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte2.structure[player.y+1][player.x]=='h' or carte2.structure[player.y+1][player.x]=='e':
                            player.movedown()
                            update()
                      
                if event.key==K_RIGHT:
                    for mobs in mobsN2:
                        if jouer == 0:
                            if mobs.x==player.x+1 and mobs.y==player.y:
                                player.image = d
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte2.structure[player.y][player.x+1]=='h' or carte2.structure[player.y][player.x+1]=='e':
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
                    
        if player.estmort:
            suite = 7
            
        #fin du niveau 2 si le joueur atteind l'arrivee
        if player.x==5 and player.y==24:
            suite = 3

    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n3.wav")
    pygame.mixer.music.play(-1)
    player.x = 30
    player.y = 47
    stuffinst()
    #meme fonctionnement que le niveau 1
    while suite == 3:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("3")
        Niveau = 3
        def_niveau.close()
        carte3.generer()
        carte3.afficher(fenetre)
        for mobs in mobsN3:
            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
        for armure in stufflist:
            if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                if armure.x == player.x and armure.y == player.y:
                        player.equiper_armure(armure)
        for arme in stufflist:
            if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
                if arme.x == player.x and arme.y == player.y:
                        player.equiper_arme(arme)
        fenetre.blit(player.image,(640,360))
        pygame.display.flip()
        for event in pygame.event.get():
            jouer = 0
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    for mobs in mobsN3:
                        if jouer == 0:
                            if mobs.x==player.x-1 and mobs.y==player.y or carte3.structure[player.y][player.x-1]=='e':
                                player.image = c
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte3.structure[player.y][player.x-1]=='h' or carte3.structure[player.y][player.x-1]=='e':
                            player.moveleft()
                            update()
                if event.key==K_UP:
                    for mobs in mobsN3:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y-1:
                                player.image = a
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte3.structure[player.y-1][player.x]=='h' or carte3.structure[player.y-1][player.x]=='e':
                            player.moveup()
                            update()

                      
                if event.key==K_DOWN:
                    for mobs in mobsN3:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y+1:
                                player.image = b
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte3.structure[player.y+1][player.x]=='h' or carte3.structure[player.y+1][player.x]=='e':
                            player.movedown()
                            update()
                      
                if event.key==K_RIGHT:
                    for mobs in mobsN3:
                        if jouer == 0:
                            if mobs.x==player.x+1 and mobs.y==player.y:
                                player.image = d
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte3.structure[player.y][player.x+1]=='h' or carte3.structure[player.y][player.x+1]=='e':
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
                    
        if player.estmort:
            suite = 7                

        #fin du niveau 2 si le joueur atteind l'arrivee
        if player.x==52 and player.y==47:
            suite = 4

    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n4.wav")
    pygame.mixer.music.play(-1)
    player.x = 30
    player.y = 47
    stuffinst()
    #meme fonctionnement que le niveau 1
    while suite==4:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("4")
        Niveau = 4
        def_niveau.close()
        carte4.generer()
        carte4.afficher(fenetre)
        for mobs in mobsN4:
            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
        for armure in stufflist:
            if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                if armure.x == player.x and armure.y == player.y:
                        player.equiper_armure(armure)
        for arme in stufflist:
            if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
                if arme.x == player.x and arme.y == player.y:
                        player.equiper_arme(arme)
        fenetre.blit(player.image,(640,360))
        pygame.display.flip()
        for event in pygame.event.get():
            jouer = 0
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    for mobs in mobsN4:
                        if jouer == 0:
                            if mobs.x==player.x-1 and mobs.y==player.y:
                                player.image = c
                                player.attack(mobs)
                                update()
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte4.structure[player.y][player.x-1]=='h' or carte4.structure[player.y][player.x-1]=='e':
                            player.moveleft()
                            update()
                if event.key==K_UP:
                    for mobs in mobsN4:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y-1:
                                player.image = a
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte4.structure[player.y-1][player.x]=='h' or carte4.structure[player.y-1][player.x]=='e':
                            player.moveup()
                            update()

                      
                if event.key==K_DOWN:
                    for mobs in mobsN4:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y+1:
                                player.image = b
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte4.structure[player.y+1][player.x]=='h' or carte4.structure[player.y+1][player.x]=='e':
                            player.movedown()
                            update()
                      
                if event.key==K_RIGHT:
                    for mobs in mobsN4:
                        if jouer == 0:
                            if mobs.x==player.x+1 and mobs.y==player.y:
                                player.image = d
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte4.structure[player.y][player.x+1]=='h' or carte4.structure[player.y][player.x+1]=='e':
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
                    
        if player.estmort:
            suite = 7

        #fin du niveau 2 si le joueur atteind l'arrivee
        if player.x==29 and player.y==6:
            suite = 5

    #musique du niveau
    pygame.mixer.music.load("Musiques/Musique n5.wav")
    pygame.mixer.music.play(-1)
    player.x = 30
    player.y = 47
    stuffinst()
    #meme fonctionnement que le niveau 1
    while suite == 5:
        hud()
        #initialisation de la carte
        def_niveau = open("carte.txt", "w")
        def_niveau.write("5")
        Niveau = 5
        def_niveau.close()
        carte5.generer()
        carte5.afficher(fenetre)
        for mobs in mobsN5:
            if mobs.x > player.x-6 and mobs.x < player.x+6 and mobs.y > player.y-6 and mobs.y < player.y+6:   
                fenetre.blit(mobs.image,(640+(mobs.x-player.x)*72,360+(mobs.y-player.y)*72))
        for armure in stufflist:
            if armure.x > player.x-6 and armure.x < player.x+6 and armure.y > player.y-6 and armure.y < player.y+6:
                fenetre.blit(armure.image,(640+(armure.x-player.x)*72,360+(armure.y-player.y)*72))
                if armure.x == player.x and armure.y == player.y:
                        player.equiper_armure(armure)
        for arme in stufflist:
            if arme.x > player.x-6 and arme.x < player.x+6 and arme.y > player.y-6 and arme.y < player.y+6:
                fenetre.blit(arme.image,(640+(arme.x-player.x)*72,360+(arme.y-player.y)*72))
                if arme.x == player.x and arme.y == player.y:
                        player.equiper_arme(arme)
        fenetre.blit(player.image,(640,360))
        pygame.display.flip()
        for event in pygame.event.get():
            jouer = 0
            if event.type == QUIT:
                        pygame.quit()
                        exit()
            if event.type == KEYDOWN:
                if event.key==K_LEFT:
                    for mobs in mobsN5:
                        if jouer == 0:
                            if mobs.x==player.x-1 and mobs.y==player.y:
                                player.image = c
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte5.structure[player.y][player.x-1]=='h' or carte5.structure[player.y][player.x-1]=='e':
                            player.moveleft()
                            update()
                if event.key==K_UP:
                    for mobs in mobsN5:
                        if jouer == 0:
                            if mobs.x==player.x and mobs.y==player.y-1:
                                player.image = a
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte5.structure[player.y-1][player.x]=='h' or carte5.structure[player.y-1][player.x]=='e':
                            player.moveup()
                            update()

                      
                if event.key==K_DOWN:
                    for mobs in mobsN5:
                        if jouer == 0:
                           if mobs.x==player.x and mobs.y==player.y+1:
                                player.image = b
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte5.structure[player.y+1][player.x]=='h' or carte5.structure[player.y+1][player.x]=='e':
                            player.movedown()
                            update()
                      
                if event.key==K_RIGHT:
                    for mobs in mobsN5:
                        if jouer == 0:
                            if mobs.x==player.x+1 and mobs.y==player.y:
                                player.image = d
                                player.attack(mobs)
                                update()
                                jouer = 1
                    if jouer !=1:
                        if carte5.structure[player.y][player.x+1]=='h' or carte5.structure[player.y][player.x+1]=='e':
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
                    
        if player.estmort:
            suite = 7                

        #fin du niveau 2 si le joueur atteind l'arrivee
        if player.x==29 and player.y==12: #and persephon mort:
            suite = 6
            
    #Boucle de fin du jeu
    while suite ==6:
        #affichage de l'image de gagne
        fond = pygame.image.load("Images/Gagne.jpg").convert()
        fenetre.blit(fond,(0,0))
        #affichage du continuer
        fenetre.blit(ok, (800, 670))
        pygame.display.flip()
        #si clic sur continuer alors sortie des boucles de niveau et recommencement du jeu
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>800  and event.pos[0]<1000 and event.pos[1]<740 and event.pos[1]>670:
                menu = 1
                suite = 0
            
    #ecran de game over  
    while suite==7:
        fond = pygame.image.load("Images/Game over.jpg").convert()
        Recommencer = font2.render("Recommencer", 1, (51,0,0))
        fenetre.blit(fond,(0,0))
        fenetre.blit(Recommencer, (800, 670))
        pygame.display.flip()
        #si clic sur continuer, sortie de toutes les boucles de niveau et recommencement du programme
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0]>800  and event.pos[0]<1000 and event.pos[1]<740 and event.pos[1]>670:
                menu = 1
                suite=0
            
    
    

    

               
        

