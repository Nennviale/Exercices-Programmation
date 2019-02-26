liste = [1,2,3,4,5,6,7,8]
print (liste[4])
'''
'''
def fonction_liste(liste): 
    fonction_liste = [1,2,3,4,5,6,7,8,9]
    return fonction_liste[5]
print(fonction_liste([1,2,3]))


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