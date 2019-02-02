import math

def to_roman_numeral(number):
    #number = 1
    unites = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dizaines = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    centaines = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

    mille = math.floor(number/1000)
    cent = math.floor((number-1000*mille)/100)
    dix = math.floor((number-1000*mille-100*cent)/10)
    un = number-1000*mille-100*cent-10*dix

    romain = ""
    if mille>0:
        romain = romain + "M"*mille
    if cent>0:
        romain = romain + centaines[cent-1]
    if dix>0:
        romain = romain + dizaines[dix-1]
    if un>0:
        romain = romain + unites[un-1]
    return(romain)