def sort_a_list(l):
    lastok = 0
    while lastok != len(l)-1:
        for i in range(lastok,len(l)-lastok):
            a = i
            b = i+1
            while b < len(l) and l[a]>=l[b]:

                temp = l[a]
                l[a] = l[b]
                l[b] = temp
                a = a+1
                b = b+1

        lastok = 0
        while lastok < len(l)-1 and l[lastok] <= l[lastok+1]:
            lastok = lastok+1
    return(l[::-1])

def sort_by_mark(my_class):
    l = []
    for i in range(len(my_class)):
        l.append(my_class[i][0])

    lastok = 0
    while lastok != len(l)-1:
        for i in range(lastok,len(l)-lastok):
            a = i
            b = i+1
            while b < len(l) and l[a]>=l[b]:
                temptuple = (my_class[a][0],my_class[a][1])
                my_class[a] = my_class[b]
                my_class[b] = temptuple

                temp = l[a]
                l[a] = l[b]
                l[b] = temp
                a = a+1
                b = b+1

        lastok = 0
        while lastok < len(l)-1 and l[lastok] <= l[lastok+1]:
            lastok = lastok+1
    return(my_class[::-1])



def takeSecond(elem):
    return elem[1]

def sort_by_name(my_class):
    sortedList = sorted(my_class, key=takeSecond)
    return(sortedList)
