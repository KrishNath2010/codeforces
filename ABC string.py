# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 08:07:29 2021

@author: Krish Nath
"""

trails=int(input())
answer_list=[]
for q in range(trails):
    leters=input()
    num1=0
    num2=0
    first=leters[0]
    last=leters[-1]
    if first==last:
        answer_list.append('NO')
        continue
    lenth=len(leters)
    for a in leters:
        if a==first:
            num1+=1
        if a==last:
            num2+=1
    if abs(num2-num1)!=lenth-(num2+num1):
        answer_list.append('NO')
        continue
    count=0
    problem=False
    if num1>num2:
        other=-1
    else:
        other=1
    for s in leters:
        if s==first:
            count+=1
        elif s==last:
            count-=1
        else:
            count+=other
        if count<0:
            answer_list.append('NO')
            problem=True
            break
    if problem==False:
        answer_list.append('YES')
    
for m in answer_list:
    print(m)