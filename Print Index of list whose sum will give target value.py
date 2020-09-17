# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:43:53 2020

@author: Nikhil Jain
"""

target = 9
li = [1,2,3,6,7]
lis= []
for i in range(0,len(li)):
    for j in range(1, len(li)):
        if li[i]+li[j] == target:
            lis.append(i)
            lis.append(j)
print(set(lis))