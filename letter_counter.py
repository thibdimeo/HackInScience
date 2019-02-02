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

alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
dictionnaire = dict()
dictionnaireII = dict()
tot = 0
reponse = ""

for i in alphabet:
    dictionnaire[i] = 0

stringe = create_string("words.txt")

for i in stringe:
    if i in dictionnaire:
        dictionnaire[i] = dictionnaire[i] + 1
        tot = tot + 1
for key in dictionnaire:
    if dictionnaire[key] > 0:
        reponse = reponse+"{0}:{1:5.2f}\n".format(key,dictionnaire[key]/tot)
print(reponse)