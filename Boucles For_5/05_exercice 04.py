# Générer une liste de carrés pour les nombres de 1 à 20
carres = []
for i in range(1, 21):
    carres.append(i ** 2)

# Afficher les carrés > 100
print("Tous les carrés :", carres)
print("Carrés > 100 :")
for val in carres:
    if val > 100:
        print(val)
