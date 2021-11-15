# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 09:19:20 2021

@author: Krish Nath
"""
def find_bigg_poss(numbers_list,w,low):
    #print("From list: ", numbers_list, ", Find for value: " , w, ", Starting at index: " , low)
    best=0
    best_index=-1
    it=0
    length = len(numbers_list)
    return binary_search(numbers_list, low, length - 1, w, best, best_index, it)

# Looking for x or smaller in the array, 'best' is the best we have found so far
def binary_search(arr, low, high, x, best, best_index, it):
    it+=1
    # Check base cases
    if x<arr[-1]:
        return best_index
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is larger than mid, then it can only
        # be present in left subarray
        elif arr[mid] < x:
            #print(it,'first')
            best = arr[mid]
            best_index=mid
            return binary_search(arr, low, mid-1, x, best, best_index, it)
 
        # Else the element can only be present in right subarray
        else:
            
            #print(it,'second')
            return binary_search(arr, mid+1, high, x, best, best_index, it)
 
    else:
        # Element is not present in the array
        return best_index

tralis=int(input())
answer_list=[]
for d in range(tralis):
    numbers_1=input().split()
    w=int(numbers_1[1])
    numbers_input=input().split()
    numbers_list=[]
    for a in numbers_input:
         numbers_list.append(int(a))
    numbers_list.sort(reverse=True)
    lenth=len(numbers_list)
    answer=0
    while numbers_list!=[]:
        answer+=1
        copied_w=w
        use_lenth=0
        biggest_poss=numbers_list[0]
        biggest_poss_index = 0
        copied_w-=biggest_poss
        numbers_list.pop(0)
        lenth-=1
        while (copied_w!=0) and (lenth > 0):
            #print(numbers_list,copied_w)
            if (numbers_list==[]):
                break
            if (lenth==biggest_poss_index):
                biggest_poss_index -= 1
            if (numbers_list[biggest_poss_index] > copied_w):
                biggest_poss_index=find_bigg_poss(numbers_list,copied_w,use_lenth)
                #print('o',biggest_poss_index,numbers_list,answer)
                if biggest_poss_index==-1:
                    break
            use_lenth=biggest_poss_index
            biggest_poss=numbers_list[biggest_poss_index]
            copied_w-=biggest_poss
            #print('kk',biggest_poss)
            numbers_list.pop(biggest_poss_index)
            lenth-=1
    answer_list.append(answer)      
for s in answer_list:
    print(s)