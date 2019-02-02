# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 23:57:31 2019

@author: User
"""
import math
def base_deux(nombre):
    decoupe = nombre
    liste = list()
    while decoupe != 0:
        digit = decoupe%2
        decoupe = math.floor(decoupe/2)
        liste.append(digit)
    return(liste)

def somme_liste(liste):
    somme = 0
    for i in liste:
        somme = somme+i
    return(somme)

def is_prime(number):
    estil = True
    for i in range(2,round(math.sqrt(number))+1):
        if (number%i) == 0:
            estil = False
            break
    
    if number == 1:
        estil = False
    return(estil)

for i in range(222281, 222381):
    if is_prime(somme_liste(base_deux(i))):
        print(i)
