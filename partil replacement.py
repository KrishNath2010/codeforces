# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:23:36 2021

@author: Krish Nath
"""

tralis=int(input())
answer_list=[]
for d in range(tralis):
    numbers_1=input().split()
    letters_1=input()
    k=int(numbers_1[0])
    n=int(numbers_1[1])
    num_of_mul=0
    for a in letters_1:
        if a=='*':
           num_of_mul+=1
    if num_of_mul>2:
        num_of_mul-=2
        times=((num_of_mul-1)//k)+1
        answer=times+2
        answer_list.append(answer)
        
    else:
        answer_list.append(num_of_mul)
for s in answer_list:
    print(s)