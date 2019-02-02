# -*- coding: utf-8 -*-
def from_roman_numeral(roman_numeral):
    nombre = roman_numeral+"I"
    tot = 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i=1
    while i < len(nombre):
        a = conv[nombre[i-1]]
        b = conv[nombre[i]]
        if a >= b:
            tot = tot+a
        else:
            tot = tot+b-a
            i = i+1
        i = i+1

    return(tot)

print(from_roman_numeral("LXXIV"))
