import csv
import os
import datetime


nom_csv = "Scores.csv"

#Compte le nombre d'essais. On affiche la solution si le mot n'a pas été trouvé.

#En cas de succès, un enregistrement du mot deviné et du nombre
#d’essais nécessaire horodaté et identifié (on demande son surnom
#au gagnant) est ajouté à un fichier csv de high scores contenant une liste d’entrées de la forme :

mot_rentrer = ""
mot_generer = ""
d

victoire = 0
#On met une variable victoire a laquel on ajoutera 1 quand le joueur aura gagné
essais = 0
#On met un compteur qui sera utile pour connaître le nombre d'essais


#//////////////#


if essais != 7:
#On dit qu'on veut que le joueur est 7 essais
    if mot_rentrer != mot_generer:
        essais += 1
         #A chaque fois que le joueur se trompe, on ajoute +1 au nombre d'essais
    else:
        victoire = 1
        #Si le joueur ne se trompe pas, il gagne, on a donc une fonction essais, et victoire qui nous permettra de faire la suite

#//////////////#


victoire = 1
if victoire == 1:

    s = input('Surnom?')
    highscore = [[mot_generer,s, essais, date]]

    fichier = open('Scores.csv', mode='r', newline = '')
    tableau_csv = csv.reader(fichier, delimiter=';')

    for ligne in tableau_csv:

        print(ligne)

        highscore.append(ligne)

    fichier.close()

    fichier_csv = open(nom_csv, mode='w', newline='')

    sortie_csv = csv.writer(fichier_csv, delimiter=';')
    sortie_csv.writerows( highscore )

    fichier_csv.close()