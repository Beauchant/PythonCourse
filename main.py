# Exercice 1
nom = "Beauchant"
print(nom)

# Exercice 2
a = 4
b = 5
somme = a + b
print(somme)

# Exercice 3
age = input("Entrez votre age: ")
print(f"Vous avez {age} ans.")

# Exercice 4
email = "beauchant509@gmail.com"
if "@" in email:
    print("Valide")
else:
    print("Non valide")

# Exercice 5
chaine = "La maison est belle!"
print(len(chaine))

# Exercice 6
couleurs = ["Rouge", "Gris", "Bleu"]
for couleur in couleurs:
    print(couleur)

# Exercice 7
valeur = 4.8
print(round(valeur))

# Exercice 8
liste_de_nombre = [3, 7, 5, 9, 2]
print(max(liste_de_nombre))

# Exercice 9
chaine1 = "J'aime la programmation"
print(chaine1.upper())

# Exercice 10
x = 3
y = 7
print(x, y)
x, y = y, x


def premiers(n):
    liste_premiers = []
    nombre = 2
    while len(liste_premiers) < n:
        est_premier = True
        for i in range(2, int(nombre**0.5) + 1):
            if nombre % i == 0:
                est_premier = False
                break
        if est_premier:
            liste_premiers.append(nombre)
        nombre += 1
    return liste_premiers


# nombres_premiers = premiers(100)
# print(nombres_premiers)