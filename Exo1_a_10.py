# 1. Afficher "Hello, World!" à l'écran.
print("\n-----------------Exo1--------------------")
print("Hello, World!")


# 2. Additionner deux nombres saisis par l'utilisateur.
print("\n-----------------Exo2--------------------")
nombre1 = input("Entrez le nombre 1: ")
nombre2 = input("Entrez le nombre 2: ")
somme = int(nombre1) + int(nombre2)
print(f"La somme de {nombre1} et {nombre2} est: {somme}")


# 3. Calculer la somme des nombres de 1 à n (saisi par l'utilisateur).
print("\n-----------------Exo3--------------------")
nombreN = input("Entrez un nombre: ")
somme1 = 0
for i in range(1, int(nombreN) + 1):
    somme1 += i

print(f"La sommme des nombres 1 à {nombreN} est: {somme1}")


# 4. Vérifier si un nombre est pair ou impair.
print("\n-----------------Exo4--------------------")
nombre_a_verifier = input("Entrez un nombre: ")
if int(nombre_a_verifier) % 2 == 0:
    print(f"{nombre_a_verifier} est un nombre pair.")
else:
    print(f"{nombre_a_verifier} est un nombre impair.")

# 5. Calculer la moyenne de trois nombres saisis par l'utilisateur.
print("\n-----------------Exo5--------------------")
accumulateur = 0
for i in range(3):
    user_nombre = int(input(f"Entrez le nombre {i + 1}: "))
    accumulateur += user_nombre

moyenne = accumulateur / 3
print(f"La moyenne des 3 nombres saisi est: {moyenne}")


# 6. Afficher les nombres de 1 à 10.
print("\n-----------------Exo6--------------------")
for i in range(1, 11):
    print(i)

# 7. Calculer la factorielle d'un nombre saisi par l'utilisateur.
print("\n-----------------Exo7--------------------")
nombre_a_factoriser = input("Entrez le nombre à factoriser: ")
factorielle = 1
for i in range(factorielle,  int(nombre_a_factoriser) + 1):
    factorielle = factorielle * i

print(f"La factorielle du nombre {nombre_a_factoriser} donne: {factorielle}")


# 8. Afficher les tables de multiplication de 1 à 10.
print("\n-----------------Exo8--------------------")
for i in range(1, 11):
    print(f"\n--Table {i}--")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")


# 9. Vérifier si un nombre est premier.
print("\n-----------------Exo9--------------------")
nombre = int(input("Entrez un nombre: "))
if nombre < 2:
    print(f"{nombre} n'est pas un nombre premier.")
else:
    for i in range(2, nombre):
        if nombre % i == 0:
            print(f"{nombre} n'est pas un nombre premier.")
            break
    else:
        print(f"{nombre} est un nombre premier.")


# 10. Inverser une chaîne de caractères.
print("\n-----------------Exo10--------------------")
chaine = "Bienvenue"
print(chaine[::-1])
