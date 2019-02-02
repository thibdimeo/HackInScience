# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:40:58 2019

@author: User
"""
import math
import itertools
def is_prime(number):
    estil = True
    for i in range(2,round(math.sqrt(number))+1):
        if (number%i) == 0:
            estil = False
            break
    
    if number == 1:
        estil = False
    return(estil)


#somme = 0
#for i in range(1000):
#    if is_prime(i):
#        somme = somme + i
#print(somme)
#
#for i in range(2,15):
#    print(120%i)


#for i in itertools.count(10):
#    if is_prime(i):
#        print(i)
#        break
    

liste = ""
for i in range(1,10):
    if is_prime(i):
        if liste == "":
            liste = str(i)
        else:
            liste = liste + ", " + str(i)
print(liste)