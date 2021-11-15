# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:12:40 2021

@author: Krish Nath
"""

tralis=int(input())
answer_list=[]
for d in range(tralis):
    lenth=int(input())
    numbers=input().split()
    count=-1
    for w in numbers:
        count+=1
        numbers[count]=int(w)
    numbers.sort()
    dup=[]
    index=0
    old=-1
    while index<lenth:
        o=numbers[index]
        if o!=old:
            old=o
            index+=1
        else:
            dup.append(o)
            numbers.remove(o)
            lenth-=1
    numbers+=dup
    answer_list.append(numbers)
for s in answer_list:
    for a in range(len(s)-1):
        print(s[a],end=' ')
    print(s[-1])
    