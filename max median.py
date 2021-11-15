# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:48:08 2021

@author: Krish Nath
"""

n_k=input().split(' ')
n=int(n_k[0])
k=int(n_k[1])
gratest=0
numbers=input().split(' ')
if n==k:
    use=[]
    for z in numbers:
        use.append(int(z))
    use.sort()
    median=n-1//2
    print(median)
for v in range(k):
    x=v+1
    for a in range(n-k+1):
        g=a+k
        if g-x<k-1:
            continue
        use_list=[]
        start=x-2
        for s in range(g-x+1):
            start+=1
            use_list.append(int(numbers[start]))
        use_list.sort()
        median_range=(g-x)//2
        median=use_list[median_range]
        if median>gratest:
            gratest=median
print(gratest)
            