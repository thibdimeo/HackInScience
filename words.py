#On recupere les mots
try:
    fichier = open('words.txt', 'r')
except FileNotFoundError:
    print("Fichier words inexistant.")

contenu = ""
for mot in fichier:
    contenu = contenu+mot

print(contenu)