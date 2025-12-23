prenom = input("Ton prénom : ")

import random

prenoms = ["Inès", "Asma", "Khrisly", "Yacine", "Ludovic", "Manon", "Lilian", "Manar", "Ahmadola", "Noemie", "Danitza"]

groupes = []

random.shuffle(prenoms)

k = 4
i = 0

while i < len(prenoms):
    groupe = prenoms[i:i+k]
    groupes.append(groupe)
    i = i + k

print(groupes)