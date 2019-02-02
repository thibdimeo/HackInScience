# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:20:57 2019

@author: User
"""

def useSecond(list):
    return(list[1])

def select_student(my_class, mini):
    
    sortedclass = sorted(my_class,key = useSecond)
    accepted = list()
    refused = list()
    for (name,grade) in sortedclass:
        if grade <= mini:
            refused.append([name,grade])
        else:
            accepted.append([name,grade])
    
    accepted = sorted(accepted, key = useSecond, reverse = True)
    
    reponse = {"Accepted": accepted, "Refused": refused}
    return(reponse)


my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]
select_student(my_class,20)