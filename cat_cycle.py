# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:14:52 2021

@author: Krish Nath
"""

trails=int(input())
answer_list=[]
for x in range(trails):
    numbers=input().split(' ')
    n=int(numbers[0])
    k=int(numbers[1])
    if n%2==0:
        answer=((k-1)%n)+1
        answer_list.append(answer)
    else:
        diff=(k-1)
        flored=diff//((n-1)/2)
        answer=int((diff+flored)%n+1)
        answer_list.append(answer)
for g in answer_list:
    print(g)