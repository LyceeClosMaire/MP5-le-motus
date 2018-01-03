import csv
import os



nom_csv = "Scores.csv"

fichier_csv = open(nom_csv, mode='w', newline='')

sortie_csv = csv.writer(fichier_csv, dialect='excel')

sortie_csv.writerow(['Bonjour'])
sortie_csv.writerow(['Aurevoir'])
fichier_csv.close()

fichier_csv = open(nom_csv, mode='r', newline='')

entree_csv = csv.reader(fichier_csv, dialect='excel')

donnes=  []

for ligne in entree_csv:
    print(ligne)
    donnes.append(ligne)

fichier_csv.close()

##"..\Csv\Scores.csv"
##"P:\DC1-0210006T\SI-Echange\ISN\MP5 Le motus\MP-Motus_Martin\Csv \Scores.csv