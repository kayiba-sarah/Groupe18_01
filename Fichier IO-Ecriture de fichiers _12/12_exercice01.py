utilisateurs = []
while True:
    nom = input(" entrer un nom d'utilisateur (ou 'stop' pour finir): ")
    if nom.lower() == "stop":
        break
    utilisateurs.append(nom)

with open("utilisateurs.txt", "w", encoding= ''utf-8'') as f:
    for u in utilisateurs:
        f.write(u + "\n")
print("Utilisateurs enregistrés dans 'utilisateurs.txt'.")
