#Générateur de table de multiplication avancé
nombre =int(input("Entrez un nombre pour sa table de multiplication :"))
#Afficher la table de multiplication de 1 à 12
print (f"==table de {nombre}==")
for i in range (1,13):
    resultat = nombre *i
    print(f"{nombre} *{i}={resultat}")
