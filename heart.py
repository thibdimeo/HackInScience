# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 23:08:26 2019

@author: User
"""

import unicodedata

liste = ""
for i in range(170000):
    if "HEART" in unicodedata.name(chr(i),'vide'):
        print(unicodedata.name(chr(i),'vide'))
        liste=liste+chr(i)
