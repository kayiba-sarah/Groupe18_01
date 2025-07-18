#inverser une chaine
texte =input ("Entrez une chaine ")
inverse =""
for char in texte :
    inverse = char + inverse
    print (f"chaine inversée : {inverse }")