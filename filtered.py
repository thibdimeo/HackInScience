def filtered(items, function):
    retour = list()
    for i in items:
        if function(i):
            retour.append(i)
    return(retour)

def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 == 1

if __name__ == "__main__":
    liste = [i for i in range(101)]
    print(", ".join(str(i) for i in filtered(liste,lambda x : x%3 == 0)))
    print(", ".join(str(i) for i in filtered(liste, lambda x: x % 5 == 0)))
    print(", ".join(str(i) for i in filtered(liste, lambda x: x % 15 == 0)))

