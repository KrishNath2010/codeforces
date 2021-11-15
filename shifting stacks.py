# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:40:34 2021

@author: Krish Nath
"""

trails=int(input())
answer_list=[]
for x in range(trails):
    number=int(input())
    numbers=input().split(' ')
    possible=True
    needed=0
    index=-1
    have=0
    for s in numbers:
        index+=1
        needed+=index
        have+=int(s)
        if have<needed:
            possible=False
    if possible==True:
        answer_list.append('YES')
    else:
        answer_list.append('NO')
for g in answer_list:
    print(g)
                