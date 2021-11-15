# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 08:44:44 2021

@author: Krish Nath
"""
answer_list=[]
q=input().split()
q=q[1]
n_list=input().split()
n_0=0
n_1=0
for l in n_list:
    if l=='0':
        n_0+=1
    else:
        n_1+=1
for a in range(int(q)):
    numbers=input().split()
    first=int(numbers[0])
    second=int(numbers[1])
    if first==1:
        if n_list[second-1]=='0':
            n_list[second-1]='1'
            n_0-=1
            n_1+=1
        else:
            n_list[second-1]='0'
            n_0+=1
            n_1-=1
    else:
        if n_1>=second:
            answer_list.append(1)
        else:
            answer_list.append(0)
for w in answer_list:
    print(w)
    
