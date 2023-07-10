# 11. Trouver la plus grande valeur dans une liste.
print("\n-----------------Exo11--------------------")
ma_liste = [4, 6, 8, 1, 3]
print(f"La plus grande valeur de la liste est: {max(ma_liste)}")


# 12. Calculer la somme des chiffres d'un nombre.
print("\n-----------------Exo12--------------------")
nombre = input("Entrez un nombre: ")
somme = 0
for i in nombre:
    somme += int(i)
print(f"La somme des chiffres de votre nombre est: {somme}")


# 13. Vérifier si une chaîne de caractères est un palindrome.
print("\n-----------------Exo13--------------------")
palindrome = input("Entrez une chaîne de caractère: ")
if palindrome[::-1] == palindrome:
    print(f"{palindrome} est un palindrome.")
else:
    print(f"{palindrome} n'est pas un palindrome.")


# 14. Afficher les nombres premiers de 1 à n (saisi par l'utilisateur).
print("\n-----------------Exo14--------------------")
print("\n-----------------Exo9--------------------")
nombre1 = int(input("Entrez un nombre: "))
liste_nombre_premier = []

if nombre1 < 2:
    print("Entrez une valeur supérieure à 1.")
else:
    for valeur in range(2, nombre1 + 1):
        est_premier = True
        for i in range(2, int(valeur**0.5) + 1):
            if valeur % i == 0:
                est_premier = False
                break
        if est_premier:
            liste_nombre_premier.append(valeur)

print(liste_nombre_premier)


# 15. Calculer la puissance d'un nombre.
print("\n-----------------Exo15--------------------")
nombre2 = int(input("Entrez un nombre: "))
puissance = int(input("Entrez la puissance: "))
resultat = nombre2 ** puissance
print(f"{nombre2} exposant {puissance} = {resultat}")

# 16. Vérifier si une année est bissextile.
print("\n-----------------Exo16--------------------")
annee = int(input("Entrez une année: "))
if annee % 4 != 0:
    print(f"{annee} n'est pas une année bissextile.")
elif (annee % 100 == 0 and annee % 400 == 0) or annee % 4 == 0:
    print(f"{annee} est une année bissextile.")

# 17. Trouver le plus petit élément dans une liste.
print("\n-----------------Exo17--------------------")
liste_element = [3, 6, 7, 9, 2]
le_plus_petit_element = min(liste_element)
print(f"Le plus petit elément de la liste est: {le_plus_petit_element}")

# 18. Calculer la moyenne d'une liste de nombres.
print("\n-----------------Exo18--------------------")
liste_nombre = [3, 6, 7, 9, 2]
moyenne = sum(liste_nombre) / len(liste_nombre)
print(f"La moyenne de la liste est: {moyenne}")

# 19. Vérifier si deux chaînes de caractères sont des anagrammes.
print("\n-----------------Exo19--------------------")
# Ex: Anagramme (listen, silent), (liste, sielt), (funeral, real fun)
chaine1 = "debit card"
chaine2 = "bad credit"

new_chaine1 = chaine1.lower().replace(" ", "")
new_chaine2 = chaine2.lower().replace(" ", "")

new_chaine1 = sorted(new_chaine1)
new_chaine2 = sorted(new_chaine2)

if new_chaine1 != new_chaine2:
    print(f"'{chaine1}' et '{chaine2}' ne sont pas des anagrammes.")
else:
    print(f"'{chaine1}' et '{chaine2}' sont des anagrammes.")

# 20. Calculer le produit des chiffres d'un nombre.
print("\n-----------------Exo20--------------------")
nombre = input("Entrez un nombre: ")
somme = 1
for i in nombre:
    somme *= int(i)
print(f"Le produit des chiffres de votre nombre est: {somme}")
