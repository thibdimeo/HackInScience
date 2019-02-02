import time

def best_collatz(fin_range = 1000, debut_range = 1):
    starttime = time.time()
    best_longueur = 0
    best_nombre = 0
    dico = dict()
    for nombre_depart in range(debut_range,fin_range):
        taille=1
        i = nombre_depart
        while i != 1:
            if i < nombre_depart:
                taille = taille+dico[i]-1
                break
            if(i%2):
                i = 3*i+1
            else:
                i = i/2
            taille = taille+1
        dico[nombre_depart] = taille
        if taille > best_longueur:
            best_longueur = taille
            best_nombre = nombre_depart
    #         print(f"Meilleur nombre : {best_nombre} : longueur de {best_longueur}")

    print(f"Meilleure chaine entre {debut_range} et {fin_range} : {best_nombre} avec une longueur de {best_longueur}")




    i = best_nombre
    chaine = [str(i)]
    while i != 1:
        if(i%2):
            i = 3*i+1
        else:
            i = i/2
        taille = taille+1
        chaine.append(str(int(i)))
    print(" -> ".join(chaine))
    stoptime = time.time()
    print(stoptime-starttime)