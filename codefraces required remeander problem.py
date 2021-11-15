# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:39:59 2021

@author: Krish Nath
"""


trails=int(input())
for x in range(trails):
    numbers=input()
    numbers_list=numbers.split(' ')
    first=int(numbers_list[0])
    y=int(numbers_list[1])
    n=int(numbers_list[2])
    new=n-y
    print((int(new//first)*first)+(y))