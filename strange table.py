# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 10:57:05 2021

@author: Krish Nath
"""

tralis=int(input())
answer_list=[]
for d in range(tralis):
    numbers_1=input().split()
    n=int(numbers_1[0])
    m=int(numbers_1[1])
    num=int(numbers_1[2])
    if num==m*n:
        answer_list.append(num)
        continue
    witght=((num-1)//n)+1
    hight=num%n
    if hight==0:
        hight=n
    row_1=m*(hight-1)
    answer=row_1+witght
    answer_list.append(answer)
for s in answer_list:
    print(s)
        