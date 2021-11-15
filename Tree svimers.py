# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:33:01 2021

@author: Krish Nath
"""
trails=int(input())
answer_list=[]
for x in range(trails):
    numbers=input().split(' ')
    p=int(numbers[0])
    a=int(numbers[1])
    b=int(numbers[2])
    c=int(numbers[3])
    if 0==p%a:
        answer_list.append(0)
        continue
    if 0==p%b:
        answer_list.append(0)
        continue
    if 0==p%c:
        answer_list.append(0)
        continue
    rem=(((p//a)+1)*a)-p
    rem_2=(((p//b)+1)*b)-p
    rem_3=(((p//c)+1)*c)-p
    if rem==rem_2 and rem_2==rem_3:
        answer_list.append(rem)
    if rem<rem_2 and rem<rem_3:
        answer_list.append(rem)
    if rem>rem_2 and rem_2<rem_3:
        answer_list.append(rem_2)
    if rem_3<rem_2 and rem>rem_3:
        answer_list.append(rem_3)
for g in answer_list:
    print(g)