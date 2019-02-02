# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 23:21:01 2019

@author: User
"""

def perfect_shuffle(deck = list()):
    shuffled = list()
    for i in range(0,int(len(deck)/2)):
        shuffled.append(deck[i])
        shuffled.append(deck[i+int(len(deck)/2)])
    return(shuffled)

print(perfect_shuffle())