import random

# Liste de mot
ma_liste = ['chercher', 'carottes', 'armement', 'elephant', 'saucisse', 'paysager','objectif', 'définies', 'ecossais', 'polaires','assiette']
# Obtenir un élément au hasard
element = random.choice(ma_liste)

mot_utilisateur = (input('Entrer un mot de 8 lettres?'))

if len(mot_utilisateur) != 8:
    print ('Ca ne fait pas 8 lettres. Essaye encore !')
else:
    print('ok')