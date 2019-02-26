# 
# Debut exo
# print (2+2)
# print (42)
# print (45*54)
# print ('ce texte')
# print ('ce texte'+'celui la')
# {
#     "vert": "arbre",
#     "bleu": "ciel",
#     "jaune": "soleil",
#     "rouge": "rubis",
# }
# {
#     8:"Lever",
#     10: "Cours",
#     14 : "RDV",
#     19 : "diner"
# }


#Exo fonction et loop
#  ma_variable=15
# if ma_variable+ 15 < 60: 
#     print ("plus petit")
# else: 
#     print ("plus grand")

# def ma_fonction(param):
#     variable = param + 3 
#     return param 

# for compteur in range(10):
#     print (compteur) 

# for compteur in range(10): 
#     print (compteur*2)
# for compteur in range(28): 
#     print (compteur*2)
'''
for compteur in range(16): 
    print (compteur*2) 
for loop in range(10):
    print (loop)

nombre = 10
for nombre in range(10):
    print(nombre) 

for nombre in range(10,0,-1):
    print (nombre)
'''

'''

Fonction
# resultat = 1
# for nombre in range(1, 6):
#     resultat = resultat * nombre
#     print(f'nombre = {nombre}')
#     print(f'resultat = {resultat}')
# print(resultat)

# test= 13%5
# print(test)

# print ('Next')
# for compteur in range(15):
#     print (compteur*2)

# print ('Next')
# for nombre in range(10,0,-1):
#     print (nombre)

# print ('Next')

# exo = (1*2*3*4*5*6)
# print (exo)

# print('JE DEFINIS LA FONCTION')

# def ma_super_fonction(liste_des_parametres):
#     print('JE SUIS EN TRAIN DE FAIRE UN MUFFIN LA')
#     print('JE POSSEDE UNE ' + liste_des_parametres)

# print('JUTILISE LA FONCTION')

# ma_super_fonction('poche a douille pleine')
# ma_super_fonction('poche a douille un peu pleine')
# ma_super_fonction('poche a douille a moitie pleine')

# def function_a_b(a, b):
#     print(a)
#     print(b)

# function_a_b("coucou", 7)

# def melanger_farine_sucre(bol, farine, sucre):
#     resultat = bol + farine + sucre
#     return resultat

# def melanger_oeuf(preparation, oeuf):
#     resultat = preparation + oeuf
#     return resultat


# melange = melanger_oeuf(
#     melanger_farine_sucre('bol', 'farine', 'sucre'),
#     'oeuf'
# )

# print(melange)

'''
'''
Exo fonction

def ma_fonction(param) :
 variable = param + 3
 return variable

resultat = ma_fonction(param=5)

def exo_fonction(param):
     variable = param*2
     return variable
resultat = exo_fonction(param=5)
print(resultat)

def liste_en_sa_longueur(nombre):
    ma_liste = [1,2,3,4,5,6]
    return ma_liste
resultat = liste_en_sa_longueur(nombre=10)
print (resultat)

ma_variable = 5
if ma_variable + 12 < 54:
 print("plus petit")
else :
 print("plus grand")

ma_variable = 5
if ma_variable < 10:
    print(ma_variable)

def affiche_inferieur_nombre(ma_variable):
    ma_variable = 5
    if ma_variable < 10:
        print (ma_variable)
    return ma_variable
resultat = affiche_inferieur_nombre(ma_variable)
print (resultat)''
'''
'''
def print_state(repre3):
    state_str = ''
    for element in repre3:
        if element == True:
            strate_str = state_str+ '1'
        else: 
            state_str = strate_str + '-'

    print(state_str)
    return
'''

