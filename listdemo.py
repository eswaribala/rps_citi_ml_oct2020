# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:57:21 2020

@author: Balasubramaniam
"""

import random

#create list
phoneNumbers=[]
#Gen Phone numbers

for _ in range(1,50):    
    phoneNumbers.append(random.randint(99952032867,99952032950))
    
    
#print phone numbers   
print ("Phone Numbers before sorting......")    
for _ in phoneNumbers:
   print(_,end="\t")    

phoneNumbers.sort()
   
print ("\nPhone Numbers after sorting......")    
for _ in phoneNumbers:
   print(_,end="\t")  
   
#nested list
   
employeeList=[1,'Arjun',[995678951,897867891],
              2,'JP',[995678952,897867892],
              3,'Vignesh',[995678953,897867894],
              4,'Shanmugam',[995678954,897867894]              
              ]

#update   
employeeList[1]='Arjun Kumar'   
#print Employee name and their phone numbers
print("\n")
for _ in employeeList:
  
   if(type(_) is str):
       print(_ , end="\t")   
   if(type(_) is list):
      for number in _:
          print (number, end="\t")  
   
   print("\n") 
   
   
list1=['NetBanking','Loan','Forex']
list2=['Chennai','Pune','Delhi']
for(x,y) in zip(list1,list2):
    print(x,"=>",y)
   
   
   
   
   
   