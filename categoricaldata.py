# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:42:10 2020

@author: Balasubramaniam
"""
import pandas as pd
df=pd.read_csv("data.csv")
print ("Dataframe", df)
print ("Shape", df.shape)
print ("Length", len(df))
print ("Column Headers", df.columns)
print ("Data types", df.dtypes)
print("Index", df.index)
print ("Values", df.values)
print(df.head(2))
print(df.tail(2))
