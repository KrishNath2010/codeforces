# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 09:42:14 2021

@author: Krish Nath
"""
import math
trails=int(input())
answer_list=[]
for q in range(trails):
    numbers=input().split()
    n=int(numbers[0])
    k=int(numbers[1])
    answer=[]
    num_answer=0
    if n==1:
        answer_list.append(0)
        continue
    half=math.ceil(k/2)
    iterat=-1
    use=0
    while use!=n:
        iterat+=1
        use=half+iterat
        if use!=k:
            answer.append(use)
            num_answer+=1
    answer_list.append(num_answer)
    answer_list.append(answer)
for m in answer_list:  
    if type(m)==list:
        for s in m:
            if s!=m[-1]:
                print(s,end=' ')  
            else:
                print(s)
    else:
        print(m)