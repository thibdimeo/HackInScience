def automaton(regle = 30, iterations = 40, largeur = 90, f = False):
    if(f):
        f.write(f"Regle : {regle}\n")
    else:
        print(f"Regle : {regle}\n")
    regle_binaire = "{0:08b}".format(regle)
    binarysubst = {'0':'.','1':'#'}

    convtab = {
    "...":binarysubst[regle_binaire[7]],
    "..#":binarysubst[regle_binaire[6]],
    ".#.":binarysubst[regle_binaire[5]],
    ".##":binarysubst[regle_binaire[4]],
    "#..":binarysubst[regle_binaire[3]],
    "#.#":binarysubst[regle_binaire[2]],
    "##.":binarysubst[regle_binaire[1]],
    "###":binarysubst[regle_binaire[0]]}

    premiere_ligne = "."*int(largeur/2)+"#"+"."*int(largeur/2)
    # premiere_ligne = '.............................................#.............................................'
    if (f):
        f.write(premiere_ligne+"\n")
    else:
        print(premiere_ligne)
    ligne = premiere_ligne
    for i in range(1,iterations):
        nouvelle_ligne = ""
        for (a,b,c) in zip(ligne,ligne[1:],ligne[2:]):
            nouvelle_ligne = nouvelle_ligne+convtab[a+b+c]
        nouvelle_ligne = convtab["."+ligne[0]+ligne[1]]+nouvelle_ligne+convtab[ligne[-2]+ligne[-1]+"."]
        ligne = nouvelle_ligne
        if f:
            f.write(nouvelle_ligne+"\n")
        else:
            print(nouvelle_ligne)

f = open("resultat.txt", "a")
for i in range(1,255):
    automaton(i,100,230,f)
f.close()