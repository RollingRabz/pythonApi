# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:28:28 2022

@author: Powernet
"""
word = input('Enter the words\n')
m = len(word)
x = m-1

        
        
result = word[:x:1] + word[x::-1]
print(result)