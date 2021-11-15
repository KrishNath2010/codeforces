# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 08:44:54 2021

@author: Krish Nath
"""

lenth=int(input())-1
numbers=input().split()
ans=0
answer=[]
while lenth!=-1:
    ele=int(numbers[lenth])
    lenth-=1
    if ele not in answer:
        ans+=1
        answer.append(ele)
print(ans)
answer=reversed(answer)
for e in answer:
    print(e, end = ' ')