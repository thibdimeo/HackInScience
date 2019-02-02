def create_string(fichier):
    # On recupere les mots
    try:
        fichier = open(fichier, 'r')
    except FileNotFoundError:
        print("Fichier words inexistant.")

    contenu = ""
    for mot in fichier:
        contenu = contenu + mot

    return(contenu)

stringe = create_string("words.txt")
count = 0
for i in stringe:
    if i is "e":
        count = count + 1

print(count)