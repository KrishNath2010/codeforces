# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 09:02:23 2021

@author: Krish Nath
"""

trails=int(input())
answer_list=[]
for d in range(trails):
    numbers=input().split()
    other=input()
    n=int(numbers[0])
    k=int(numbers[1])
    if k==n/2:
        answer_list.append('NO')
        continue
    first=[]
    last=[]
    for o in range(k):
        n-=1
        first.append(other[o])
        last.append(other[n])
    if first==last:
        answer_list.append('YES')
    else:
        answer_list.append('NO')
for e in answer_list:
    print(e)