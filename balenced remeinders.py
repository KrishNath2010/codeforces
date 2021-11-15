# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 21:11:00 2021

@author: Krish Nath
"""
trails=int(input())
divisible_number=3
answer_list=[]
for x in range(trails):
    number=int(input())
    numbers=input().split(' ')
    avg=int(number/3)
    c_0=0
    c_1=0
    c_2=0
    for s in numbers:
        use=int(s)
        mod=use%3
        if mod==0:
            c_0+=1
        elif mod==1:
            c_1+=1
        else:
            c_2+=1
    result=0
    c_list=[]
    c_list.append(c_0)
    c_list.append(c_1)
    c_list.append(c_2)
    while c_2!=c_1 or c_1!=c_0:
        if c_0<=c_1 and c_0<=c_2:
            lowest=0 
        elif c_1<=c_0 and c_1<=c_2:
            lowest=1 
        else:
            lowest=2 
        c_list[lowest]+=1
        c_list[(lowest-1)%3]-=1
        c_0=c_list[0]
        c_1=c_list[1]
        c_2=c_list[2]
        result+=1
    answer_list.append(result)
for g in answer_list:
    print(g)
        
        