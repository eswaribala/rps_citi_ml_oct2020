# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 13:37:50 2020

@author: Balasubramaniam
"""

print("Read Personal Data")
#reading input
name=input("Enter Name")
#type checking
print(type(name))
#type conversion
age=int(input("Enter Age"))
print(type(age))

#print the output
#data formatters
print("Name=%s\n Age=%d" %(name,age))


#complex number
print(complex(45,67))


from datetime import date

print(date.today().strftime("%d/%m/%y"))


import datetime
dob=datetime.date(1970,12,2)
print(dob.strftime("%d/%m/%y"))

#for loop 
for _ in name[0:]:
    print(_)




