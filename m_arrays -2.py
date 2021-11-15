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
    half=m/2
    s=[]
    f=[]
    for d in range((m//2)+1):
        s.append(0)
        f.append(0)
    for a in numbers_2:
        use=int(a)
        #print(use)
        mod=use%m
        if mod==0:
            f[0]+=1
            #print('f')
        else:
            if mod==m/2:
                res=0
            elif mod>(m//2):
                mod=m-mod
                res=-1
            else:
                res=1
            #print('s',res)
            s[mod]+=res
            #print('f')
            f[mod]+=1
    index=-1
    #print('s',s,'f',f)
    #print('curr',answer)
    for b in s:
        #print(b,'b')
        index+=1
        if f[index]!=0:
            answer+=1
        if index==0:
            continue
        if (((b<-1) or (b>1)) and (f[index]))!=0:
            #print(b,'b')
            answer+=(abs(b)-1)
    answer_list.append(answer)
for s in answer_list:
    print(s)
        
    