mini = 0
maxi = 1000
for i in range(mini,maxi-mini+1):
    if i%7 == 0:
        digits = [int(digits) for digits in str(i)]
        somme = 0

        for j in digits:
            somme = somme+j

        if somme%3 == 0:
            print(i)
