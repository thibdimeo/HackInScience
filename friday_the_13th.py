# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:40:30 2019

@author: User
"""
import datetime

def friday_the_13th():
    now = datetime.datetime.now()
    jour = datetime.date.weekday(now)
    
    if jour < 4:
        vendredi = 7-3-jour
    else:
        vendredi = 7-jour+4
    
    vendredipro = datetime.datetime.now()+datetime.timedelta(days=+vendredi)
    
    while vendredipro.day != 13:
        vendredipro = vendredipro+datetime.timedelta(days=+7)
    
    print(vendredipro.date())
    


friday_the_13th()

