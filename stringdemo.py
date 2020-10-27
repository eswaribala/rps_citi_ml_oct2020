# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:20:12 2020

@author: Balasubramaniam
"""

import random

#control statement
for _ in range(1,100):
    genNumber=random.randint(501,5001)
    #conditional statement
    if(genNumber>1500):
        print(genNumber,end="\t")
     
        
import base64
#encoding
seqNo=456
genSeq=base64.b64encode(str(seqNo).encode(encoding='utf-8', errors='strict')) 
print("\n %s" %(genSeq))      

#decoding

#justification with fillers
organizationName="Citi Corp"
print(organizationName.center(len(organizationName)+30,"*"))
print(organizationName.ljust(len(organizationName)+30,"*"))
print(organizationName.rjust(len(organizationName)+30,"*"))















