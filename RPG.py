'''
Exo liste
liste = [1,2,3,4,5,6,7,8]
print (liste[4])
'''
'''
def fonction_liste(liste): 
    fonction_liste = [1,2,3,4,5,6,7,8,9]
    return fonction_liste[5]
print(fonction_liste([1,2,3]))
'''

'''
def print_state(repr3):
    state_str = ''

    for element in repr3:
        if element == True:
            state_str = state_str + '1'
        else:
            state_str = state_str + '-'

    print(state_str)
    return

state = [False, False, False, True, False, False, False, False, False, False, ]
print_state(repr3=state)

other_state = [True, False, False, False, False, False, False, False, False, False, ]
print_state(repr3=other_state)
'''
'''

Exo liste
table_multiplication = liste = [1,2,3,4]
print (table_multiplication)

liste = [[1,2,3,4], [5,6,7,8],[9,10,11,12], [13,14,15,16]]
print(liste)
liste[0]
print(liste[0])
for number in liste:
    print (number)
for sousliste in liste:
    for element in sousliste:
        print (element)


def print_matrice(matrice):
    print("print_matrice")
    print(matrice)
    for sousliste in matrice:
        for element in sousliste:
            print (element, end='\t')
        print ('')
    return 

mlemaudit= [[10,2,3], [4,5,6],[7,8,9]]
print_matrice(mlemaudit)

chocolat= [[1246,9037,8576], [4598,5323,6567],[7098,2348,9045]]
print_matrice(chocolat)



def create_matrice(longueur, largeur):
    print(longueur)
    print(largeur)
    print ("pour eviter")

    for j in range(largeur+1):
        for i in range(longueur+1): 
            print (f'({i}, {j})')

create_matrice(3, 2)
'''


'''

Exo Dico

Définir un dictionnaire qui contient la valeur 150 pour la clé “soda”, la valeur 50 pour la clé “pâtes” et la valeur 2 pour la clé “champignons”.
Définir une fonction qui renvoie le nombre de jours d’un mois. Par exemple : nb_jours("Mars") renvoie 31. On suppose que l’année en cours n’est pas bisextile.
Même exercice que précédemment, mais on prend en compte les années bisextiles.
'''
'''
print("exo 1")
dico = {'soda':150,'pates': 50,'champignons': 2  }
print(dico)



print("exo 2")


mois ={'janvier':31, 'fevrier':28,'mars': 31, 'avril':30}
def cherche_nombre_jour(mois_a_chercher):
    return mois.get(mois_a_chercher) 

cherche_nombre_jour('mars')
print(cherche_nombre_jour)



joueur = {'name': 'Arthur','level': 35, 'inventory': ['sac','lampe','couteau']}
print(joueur)


Exo : Jeu Snake
print('Debut du jeu')

def print_state(repr3):
    state_str = ''

    for element in repr3:
        if element == True:
            state_str = state_str + '1'
        else:
            state_str = state_str + '-'

    print(state_str)
    return

state = [False, False, False, True, False, False, False, False, False, False, ]
print_state(repr3=state)

other_state = [True, False, False, False, False, False, False, False, False, False, ]
print_state(repr3=other_state)

'''


""" 
Exo RPG
Definir une fonction qui prends en compte le personnage, son level et son inventaire
    Args : 
        Un dictionnaire: 
        dico :{'name':'Arthur','level':35,'inventory',['sac','lamp','knife']}   
    Returns :
        Dico 
"""


def affiche_joueur(dico):
    dico = {'name':'Arthur','level':35,'inventory':['sac','lamp','knife']}
    print(dico)
infoperso= {'name':'Arthur','level':35,'inventory':['sac','lamp','knife']}
affiche_joueur(infoperso)
print(f"Je suis Arthur, level 35 et voici mon inventaire : [sac,lamp,knif]")
print(infoperso.get('name'))
print(infoperso.get('name') + str(infoperso.get('level'))+ str(infoperso.get('inventory')))
print(f"{infoperso.get('name')} prout")
print(f"Je suis {infoperso.get('name')}, level {infoperso.get('level')}, et mon inventaire contient {infoperso.get('inventory')}")