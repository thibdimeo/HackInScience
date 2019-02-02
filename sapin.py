import sys

def sapin(taillesapin):
    sapin = []
    largeur = 1
    moins = 2
    largeurpied = 1
    for i in range(1,taillesapin+1):
        for j in range(1,i+4):
            sapin.append("*"*largeur)
            largeur = largeur + 2
        if i % 2 == 0:
            moins = moins+2
        largeur = largeur-moins
        if i % 2 == 0:
            largeurpied = largeurpied + 2

    sapin = [" "*(int((len(sapin[-1]))/2)-int(len(i)/2))+i for i in sapin]

    for i in sapin:
        print(i)

    for i in range(1,taillesapin+1):
        print(" "*int((len(sapin[-1]))/2-int(largeurpied/2))+"|"*largeurpied)

# print(type(sys.argv[1]))
# if len(sys.argv) == 2:
#     sapin(int(sys.argv[1]))
# else:
#     print("Must have an integrer parameter")

sapin(0)
