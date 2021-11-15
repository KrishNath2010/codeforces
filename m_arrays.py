# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:44:06 2021

@author: Krish Nath
"""

tralis=int(input())
answer_list=[]
for d in range(tralis):
    numbers_1=input().split()
    numbers_2=input().split()
    n=int(numbers_1[0])
    m=int(numbers_1[1])
    answer=0
    mod_list=[]
    half=m/2
    half_poss=0
    _0_poss=0
    for a in numbers_2:
        use=int(a)
        mod=use%m
        if mod==0:
            _0_poss=1
            continue
        elif mod==half:
            half_poss=1
            continue
        mod_list.append(mod)
    answer+=(half_poss+_0_poss)
    pairs=[]
    for d in range((m//2)+1):
        if d!=0 or d!=half:
            pairs.append((d,m-d))
    for h in pairs:
        #print(h,mod_list)
        p=mod_list.count(h[0])
        q=mod_list.count(h[1])
        #print(p,q,answer)
        diff=abs(p-q)
        if diff==0 or diff==1:
            n_l=1
        else:
            n_l=diff
        if p==0 and q==0:
            n_l=0
        answer+=n_l
    answer_list.append(answer)
for s in answer_list:
    print(s)
        
    