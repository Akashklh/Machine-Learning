# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 12:49:16 2021

@author: Akash
"""

#-------------------------Reading & Writing data in Files----------------------

import pandas

# Reading CSV Files with Pandas:
df = pandas.read_csv('C:/Users/91988/Desktop/python Library/files/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
df.to_csv('IIT-B.csv')

# Reading Excel Files with Pandas
df1 = pandas.read_excel('C:/Users/91988/Desktop/python Library/files/User_Data.xlsx')

df1 = pandas.read_excel('User_Data.xlsx')
print(df1)

# Writing Excel Files with Pandas 
df1.to_excel('IIT-B.xlsx')
df2 = pandas.DataFrame(df1)
print (df2)


