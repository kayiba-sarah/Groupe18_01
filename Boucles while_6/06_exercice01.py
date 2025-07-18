import random

# Générer un nombre aléatoire entre 1 et 100
nombre_secret = random.randint(1, 100)
essai = None

# Boucle tant que l'utilisateur n'a pas trouvé le nombre
while essai != nombre_secret:
    essai = int(input("Devine le nombre (1-100) : "))
    if essai < nombre_secret:
        print("Trop petit.")
    elif essai > nombre_secret:
        print("Trop grand.")
    else:
        print("Bravo, tu as trouvé !")
