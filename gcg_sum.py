# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:26:43 2021

@author: Krish Nath
"""
import math
tralis=int(input())
answer_list=[]
def get_sum(n):
    ans=0
    for a in str(n):
        ans+=int(a)
    return ans
for d in range(tralis):
    m=int(input())
    while True:
        sum_m=get_sum(m)
        if math.gcd(m, sum_m)>1:
            answer_list.append(m)
            break
        else:
            m+=1
for s in answer_list:
    print(s)