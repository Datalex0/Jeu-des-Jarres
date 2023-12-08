##################
# Jeu des Jarres #
##################

import random
import time
from art import *

#variable pour recommencer le jeu
retry = "o"
'''

*** Célèbre Jeu des Jarres ***

*** Règles du Jeu ***

Vous avez 5 Jarres. Il faut choisir entre une des 5 Jarres pour obtenir une clé. 
Si vous obtenez une clé, le jeu continue. Si vous tombez sur le Serpent, vous perdez une clé.
Défaite : Vous tombez sur le Serpent et vous n'avez pas de clé.
Victoire : Vous obtenez 3 clés.

Les Niveaux :
Niveau 1 : 4 clés / 1 Serpent
Niveau 2 : 3 clés / 2 Serpents
Niveau 3 : 1 clé / 4 Serpents

'''

def again():
    time.sleep(1)
    replay = input("On recommence ? (o/n) : ")
    print(" ")

    if replay == "n":
        print("")
        print(f"Ok, merci d'avoir joué {joueur}. A+ ")
        time.sleep(1)
        return "n"

    elif replay == "o":
        print(f"Super {joueur} ! On recommence !")
        print("...")
        time.sleep(1)
        return "o"

    else :
        print("Oops..")
        return again()
    


while retry == "o":


    print("\n")
    tprint("Jeu des Jarres")
    print("\n")
    print("Essaie d'otenir 3 clés.")
    print("Enjoy !")
    print("\n")

    nb_clés = 0


    #le joueur entre son nom et celui de son adversaire
    joueur = input("Entres ton nom : ")

    def choix_niveau():
        time.sleep(1)
        niveau = input("Choisis ton niveau (1, 2 ou 3) : ")
        print("\n")

        #établissement des jarres
        if niveau=="1":
            seq=["Clé","Clé","Clé","Clé","Serpent"]
        elif niveau=="2":
            seq=["Clé","Clé","Clé","Serpent","Serpent"]
        elif niveau=="3":
            seq=["Clé","Serpent","Serpent","Serpent","Serpent"]
        else :
            print("Oops..")
            return choix_niveau()
        
        return seq


    seq = choix_niveau()

    #nécessité des 3 clés
    while nb_clés >=0 and nb_clés < 3 :
        
        
        #initialisation des jarres
        random.shuffle(seq)

        #choix du joueur
        def choix_jar():

            jar_chois = input("Choisis parmi les Jarres 1, 2, 3, 4 et 5 : ")

            if jar_chois=="1":
                choix=seq[0]
            elif jar_chois=="2":
                choix=seq[1]
            elif jar_chois=="3":
                choix=seq[2]
            elif jar_chois=="4":
                choix=seq[3]
            elif jar_chois=="5":
                choix=seq[4]
            else:
                print("Oops..")
                return choix()

            return choix

        choix = choix_jar()

        # Si le joueur tombe sur une clé
        if choix == "Clé":
            time.sleep(1)
            print("Bravo ! C'est une clé !")
            nb_clés += 1
        # Si le joueur tombe sur un Serpent
        elif choix == "Serpent":
            time.sleep(1)
            print("Aïe.. c'est un Serpent !")
            nb_clés -= 1
            if nb_clés>=0:
                time.sleep(1)
                print("Tu perds une clé !")
            else:
                time.sleep(1)
                print("Tu n'avais plus de clé.")

        #Si le joueur a 3 clés : victoire
        if nb_clés==3:
            time.sleep(1)
            print("Bravo !!!")
            time.sleep(1)
            print("Tu possèdes 3 clés et tu as donc gagné !")
            time.sleep(1)
            print("Félicitations :) ")
            retry=again()
        #Si le joueur a entre 0 et 3 clés : ça continue
        elif nb_clés>=0:
            time.sleep(1)
            if nb_clés == 0 :
                print(f"Attention ! Tu n'as plus de clé, tu n'as plus le droit à l'erreur !")
            elif nb_clés == 1 :
                print(f"Tu as {nb_clés} clé !")
            else:
                print(f"Tu as {nb_clés} clés !")
            time.sleep(1)

        #Si le joueur perd une clé alors qu'il n'en avait pas : Défaite 
        else:
            time.sleep(1)
            print("Tu as perdu :(")
            retry = again()
            if retry == "n":
                break
