# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:46:12 2020

@author: Nikhil Jain
"""

li2= ['nikhil jain' ,'santhosh gowda', 'nikhil shetty']
li3= []

#Split by First name

for i in li2:    
    li3.append(i.split(' ')[0])
li3

#Create a list of wordcount of each word 
wordcount = []
for word in li3:
    wordcount.append(li3.count(word))

wordcount 

#Create a dictionary with wordcount and value
dict = {}
for key in li3:
    for values in wordcount:
        dict[key] = values
        wordcount.remove(values)
        break
dict        
#Print most frequently occuring word
max_key = max(dict, key = dict.get)
print(max_key)
