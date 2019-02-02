# -*- coding: utf-8 -*-
alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
for i in range(0,26):
    for j in range(i+1,26):
        print("{}{}".format(alphabet[i],alphabet[j]))
