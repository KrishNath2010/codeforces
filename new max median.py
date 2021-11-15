# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:09:37 2021

@author: Krish Nath
"""
import sys
sys.setrecursionlimit(10**9)
#import random
my_dict={} 
def mediean(n_list,n,start,end):    
    use=[]
    for z in range(start-1, end):
        use.append(int(n_list[z]))
    use.sort()
    median=((n+1)//2)-1
    #print('start',start,'end',end,'index',median)
    #print(use)
    #print(use[median])
    return use[median]

def max_median(n_list,n,k,start,end):
    key=(end*1000000+start)
    if (key in my_dict):
        #print('helped by modification', start, end)
        return (my_dict.get(key))

    if n==k:
        ret_val=mediean(n_list,n,start,end)
    else:
        choice_1=max_median(n_list,n-1,k,start+1,end)
        choice_2=max_median(n_list,n-1,k,start,end-1)
        choice_3=mediean(n_list,n,start,end)
        #print(choice_1,choice_2,choice_3,'choices')
        ret_val= max(choice_1,choice_2,choice_3)
        #put ret_val for start to end in my_dict
    my_dict[key]=ret_val
    #print('added modification', start, end)
    return ret_val  

n_k=input().split(' ')
n=int(n_k[0])
k=int(n_k[1])
gratest=0
numbers=input().split(' ')
#numbers=[]
# for q in range(200000):
#     numbers.append(random.randint(1, 200000))    
print(max_median(numbers,n,k,1,n))