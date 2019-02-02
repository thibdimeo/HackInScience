# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 23:38:56 2019

@author: User
"""

f0 = 0
f1 = 1
fibliste = "1"
for i in range(9):
    fibliste = fibliste+', '
    fibN = f0 + f1
    f0 = f1
    f1 = fibN
    fibliste = fibliste+str(fibN)
fibliste = fibliste+'.'

print(fibliste)