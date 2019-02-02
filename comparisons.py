# -*- coding: utf-8 -*-

the_list = [14326111111116561, 111, 312377936, 1027708881, 1495785517,
            1858250798, 1693786723, 1871000655963, 374455497, 4301541414141414141418267]
max = 0
for i in range(1,len(the_list)):
    if the_list[i] > the_list[max]:
        max = i

print(the_list[max])