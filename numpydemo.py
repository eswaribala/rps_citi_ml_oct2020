# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:23:10 2018

@author: Balasubramaniam
"""
#multi dimensional array
import numpy as np
#Create a multidimensional array as follows:
m = np.array([np.arange(3), np.arange(3),np.arange(3)])
print(m)
#Show the array shape as follows:
print(m.shape)



#single precision floats
print(np.arange(7, dtype='f'))#[ 0.  1.  2.  3.  4.  5.  6.]
#complex number array
print(np.arange(7, dtype='D'))#[ 0.+0.j  1.+0.j  2.+0.j  3.+0.j  4.+0.j  5.+0.j  6.+0.j]
#slicing
a = np.arange(9)
print(a[3:])#[3 4 5 6 7 8]
#choose elements from indexes the 0 to 7 with an increment of 2:
print(a[:7:2])#[0 2 4 6]
#negative indices and reverse the array
print(a[::-1])#[8 7 6 5 4 3 2 1 0]
#flattening the array
b = np.arange(24).reshape(2,3,4)
print(b)
print(b.ravel())#view of original array
print(b.flatten())#flatten returns the copy

#reshape
b.shape=(6,4)
print(b)
#transpose
print(b.transpose())
#resize
b.resize((2,12))
print(b)
#stacking array
a = np.arange(9).reshape(3,3)
print(a)
b=2*a
print(b)
#horizontal stacking
print(np.hstack((a, b)))
print(np.concatenate((a, b), axis=1))#hstack equivalent
#vstack
print(np.vstack((a, b)))
print(np.concatenate((a, b), axis=0))#vstack equivalent 
#number of dimensions
a=np.array([[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]])
print(a.ndim)
print(a.size)







