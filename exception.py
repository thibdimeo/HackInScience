# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:42:55 2019

@author: User
"""
import sys
try:
    print(sys.argv[1])
except IndexError:
    print("Not enough parameters.")

