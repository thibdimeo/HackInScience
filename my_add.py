# -*- coding: utf-8 -*-
import sys

addition = 0

if len(sys.argv) > 1:
    for i in range(1,len(sys.argv)):
        addition = addition + int(sys.argv[i])
    print(addition)
else:
    print("usage: python3 solution.py OP1 OP2")
