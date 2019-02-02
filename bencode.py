
def encode(variable):
    if type(variable) == set:
        raise TypeError("Type Set non reconnu.")
    if type(variable) == str:
        raise TypeError("Type Str non reconnu.")
    elif type(variable) == int:
        reponse = (lambda x: 'i' + str(x) + 'e')(variable)
    elif type(variable) == bytes:
        reponse = (lambda x: str(len(x.decode())) + ":" + (x.decode()))(variable)
    elif type(variable) == list:
        reponse = ""
        for i in variable:
            reponse = reponse + (encode(i)).decode()
        reponse = "l" + reponse + "e"
    elif type(variable) == dict:
        reponse = ""
        for (key) in variable:
            if type(key) == bytes:
                reponse = reponse + encode(key).decode() + encode(variable[key]).decode()
            else:
                raise TypeError("Cle du dictionnaire doit etre un byte")
        reponse = "d" + reponse + "e"
    return reponse.encode()


def decode_int(entree):
    i = 1
    entier = ""
    try:
        while entree[i] != ord("e"):
            entier = entier + chr(entree[i])
            i = i + 1
        return (int(entier), i + 1)
    except Exception as err:
        print("Un chiffre est mal codé !",err)


def decode_str(entree):
    u = 0
    longueur = ""
    while entree[u] != ord(":"):
        longueur = longueur + chr(entree[u])
        u = u + 1

    longueur = int(longueur)

    mot = ""
    try:
        for i in range(u + 1, longueur + u + 1):
            mot = mot + chr(entree[i])
        return (mot.encode(), i + 1)
    except Exception as err:
        print("Un mot est mal codé !", err)



def decode_list(entree):
    i = 1
    liste = list()
    try:
        while entree[i] != ord(b"e"):
            if entree[i] in b"123456789":  # Ca commence par un chiffre c'est donc un string
                decoded = decode_str(entree[i:])
                liste.append(decoded[0])
                i = i + decoded[1]
            elif entree[i] == ord("l"):  # Ca commence par un L c'est donc une liste
                decoded = decode_list(entree[i:])
                liste.append(decoded[0])
                i = i + decoded[1]
            elif entree[i] == ord("i"):  # Ca commence par un i c'est donc un chiffre
                decoded = decode_int(entree[i:])
                liste.append(decoded[0])
                i = i + decoded[1]
            elif entree[i] == ord("d"):  # Ca commence par un d c'est donc un dictionnaire
                decoded = decode_dict(entree[i:])
                liste.append(decoded[0])
                i = i + decoded[1]
        return ([liste, i + 1])
    except Exception as err:
        print("Une liste est mal codée !", err)





def decode_dict(entree):
    i = 1
    dictionnaire = dict()
    try:
        while entree[i] != ord(b"e"):
            # la premiere clef est une string donc on le cherche directement sinon erreur
            if entree[i] in b"123456789":
                decoded = decode_str(entree[i:])
                clef = decoded[0]
                i = i + decoded[1]
            else:
                raise TypeError("Une clef du dictionnaire n'est pas un mot batard")

            # On regarde ensuite quel est l'objet suivant
            if entree[i] in b"123456789":  # Ca commence par un chiffre c'est donc un string
                decoded = decode_str(entree[i:])
                valeur = decoded[0]
                i = i + decoded[1]
            elif entree[i] == ord("l"):  # Ca commence par un L c'est donc une liste
                decoded = decode_list(entree[i:])
                valeur = decoded[0]
                i = i + decoded[1]
            elif entree[i] == ord("i"):  # Ca commence par un i c'est donc un chiffre
                decoded = decode_int(entree[i:])
                valeur = decoded[0]
                i = i + decoded[1]
            elif entree[i] == ord("d"):  # Ca commence par un d c'est donc un dictionnaire
                decoded = decode_dict(entree[i:])
                valeur = decoded[0]
                i = i + decoded[1]

            # On rentre ensuite la clef et la valeur
            dictionnaire[clef] = valeur
        return ([dictionnaire, i + 1])
    except Exception as err:
        print("Un dictionnaire est mal codé !", err)

def decode(entree):
    i = 0
    while i < len(entree):
        # On regarde ensuite quel est l'objet suivant
        if entree[i] in b"123456789":  # Ca commence par un chiffre c'est donc un string
            decoded = decode_str(entree[i:])
            i = i + decoded[1]
        elif entree[i] == ord("l"):  # Ca commence par un L c'est donc une liste
            decoded = decode_list(entree[i:])
            i = i + decoded[1]
        elif entree[i] == ord("i"):  # Ca commence par un i c'est donc un chiffre
            decoded = decode_int(entree[i:])
            i = i + decoded[1]
        elif entree[i] == ord("d"):  # Ca commence par un d c'est donc un dictionnaire
            decoded = decode_dict(entree[i:])
            i = i + decoded[1]
    return (decoded[0])
#
# decode(encode(5))
# decode(encode(b"mot"))
# decode(encode([5,2]))
# decode(encode([[[]]]))
# decode(encode(b"a"))
# encode({b"5": {b"3":5}})
# {b"5": {b"3":5}}
# encode({b"erg" : 5,"5" : [5,3]})
#
# dico = {b"5": {b"3":5}}
# dico_encode = encode(dico)
# decode(dico_encode)
#
# dico2 = {b"ste": 5}
# encode(dico2)
