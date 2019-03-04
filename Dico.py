'''
Définir un dictionnaire qui contient la valeur 150 pour la clé “soda”, la valeur 50 pour la clé “pâtes” et la valeur 2 pour la clé “champignons”.
Définir une fonction qui renvoie le nombre de jours d’un mois. Par exemple : nb_jours("Mars") renvoie 31. On suppose que l’année en cours n’est pas bisextile.
Même exercice que précédemment, mais on prend en compte les années bisextiles.
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


