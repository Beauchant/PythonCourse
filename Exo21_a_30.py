# 21. Trouver tous les diviseurs d'un nombre.
print("\n-----------------Exo21--------------------")
nombre = int(input("Entrez un nombre: "))
liste_diviseur = []
for i in range(1, nombre + 1):
    if nombre % i == 0:
        liste_diviseur.append(i)

print(f"Les diviseurs de {nombre} sont:", *liste_diviseur, sep=", ")


# 22. Vérifier si une chaîne de caractères est un palindrome en ignorant les espaces.
print("\n-----------------Exo22--------------------")
# Ex : palindrome "Engage le jeu que je le gagne"
chaine = "Engage le jeu que je le gagne"

new_chaine = chaine.lower().replace(" ", "")
if new_chaine == new_chaine[::-1]:
    print(f"'{chaine}', est un palindrome.")
else:
    print(f"'{chaine}', n'est pas un palindrome.")


# 23. Calculer la somme des carrés des nombres de 1 à n.
print("\n-----------------Exo23--------------------")
# Formule n(n + 1)(2n + 1) / 6
n = int(input("Entrez un nombre: "))
somme_des_carres = n * (n + 1) * ((2*n) + 1) // 6
print(f"Somme des carrés des nombres de 1 à {n} est: {somme_des_carres}")


# 24. Compter le nombre de voyelles dans une chaîne de caractères.
print("\n-----------------Exo24--------------------")
chaine_de_caractere = "La maison est belle!"
voyelle = "aeiouy"
nombre_de_voyelle = 0
for i in chaine_de_caractere:
    if i in voyelle:
        nombre_de_voyelle += 1

print(f"Le nombre de voyelle dans votre chaine de caractère est: {nombre_de_voyelle}")


# 25. Vérifier si une chaîne de caractères est un pangramme.
print("\n-----------------Exo25--------------------")
# Ex : "Portez ce vieux whisky au juge blond qui fume"
import string

chaine_d_caractere = "Portez ce vieux whisky au juge blond qui fume".lower()
alphabet_francais = string.ascii_lowercase

count = 0
for i in alphabet_francais:
    if i in chaine_d_caractere:
        count += 1

if count == len(alphabet_francais):
    print("Votre chaîne de caractère est un pangramme.")
else:
    print("Votre chaîne de caractère n'est pas un pangramme.")


# 26. Trouver tous les nombres parfaits de 1 à n.
print("\n-----------------Exo26--------------------")
nombre_parfait = int(input("Entrez un nombre: "))
somme_diviseur = 0
for i in range(1, nombre_parfait):
    if nombre_parfait % i == 0:
        somme_diviseur += i

if nombre_parfait == somme_diviseur:
    print(f"{nombre_parfait} est un nombre parfait.")
else:
    print(f"{nombre_parfait} n'est pas un nombre parfait.")


# 27. Vérifier si un nombre est un nombre de Fibonacci.
print("\n-----------------Exo27--------------------")
# Un nombre de Fibonacci si et seulement si l'une des deux expressions
# (5n^2 + 2) ou (5n^2 - 2) est un carré parfait.

nombre_fibonacci = int(input("Entrez un nombre: "))
expression1 = ((5 * nombre_fibonacci) ** 2 + 2)
expression2 = ((5 * nombre_fibonacci) ** 2 - 2)

carre_parfait1 = expression1 ** 0.5
carre_parfait2 = expression2 ** 0.5

if ".0" in str(carre_parfait1) or ".0" in str(carre_parfait2):
    print(f"{nombre_fibonacci} est un nombre de Fibonacci.")
else:
    print(f"{nombre_fibonacci} n'est pas un nombre de Fibonacci.")


# 28. Calculer le nombre de jours entre deux dates
print("\n-----------------Exo28--------------------")
from datetime import datetime

# Définir les dates de début et de fin
date_debut = datetime(2023, 7, 10)
date_fin = datetime(2023, 7, 13)

# Calculer la différence entre les dates
difference = date_fin - date_debut

# Extraire le nombre de jours de la différence
nombre_jours = difference.days

# Afficher le résultat
print(f"Le nombre de jours entre les deux dates est: {nombre_jours}")


# 29. Vérifier si un mot est un anagramme d'un autre mot.
print("\n-----------------Exo29--------------------")
# Ex : Anagramme (listen, silent), (liste, sielt)
mot1 = "listen"
mot2 = "silent"

new_mot1 = mot1.lower().replace(" ", "")
new_mot2 = mot2.lower().replace(" ", "")

new_mot1 = sorted(new_mot1)
new_mot2 = sorted(new_mot2)

if new_mot1 != new_mot2:
    print(f"'{mot2}' n'est pas un anagrammes de '{mot1}'.")
else:
    print(f"'{mot2}' est un anagrammes de '{mot1}'.")

# 30. Convertir un nombre binaire en décimal.
print("\n-----------------Exo30--------------------")
nombre_binaire = input("Entrez un nombre binaire: ")
nombre_decimal = int(nombre_binaire, 2)
print(f"Le nombre binaire {nombre_binaire} donne {nombre_decimal} en décimal.")
