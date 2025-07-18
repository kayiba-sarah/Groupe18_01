prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
mettier = input("Entrez votre métier : ")

jours_vécus = age * 365

print("\n== PROFIL UTILISATEUR ==")
print(f"Prénom : {prenom}")
print(f"Age : {age} ans ({jours_vécus} jours vécus environ)")
print(f"Ville : {ville}")
print(f"Métier : {mettier}")
