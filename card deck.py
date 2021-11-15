# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:38:16 2021

@author: Krish Nath
"""
def find_max_index(comb,lenth,maximum):
    if ((comb[-1])[-1])==maximum:
        return lenth-1 
    elem_index=1
    print('len',lenth)
    prev_max = 0
    while True:
        print("loop1", elem_index)
        list_index=lenth-1
        found_unique_max=True
        curr_max=0
        curr_max_index=list_index
        while list_index>=0:
            print("loop2", list_index)
            curr_list=comb[list_index]
            print('current_list',curr_list, "len", len(curr_list))
            if elem_index>(len(curr_list)-1):
                if (prev_max == maximum):
                    list_index-=1
                    break
                print('0 returning',list_index)
                return list_index
            curr_elm=curr_list[elem_index]
            print("curr_elm set to", curr_elm)
            if curr_elm>curr_max:
                print('found new max','old',curr_max,'new',curr_elm)
                curr_max=curr_elm
                curr_max_index=list_index
                found_unique_max=True
            elif curr_elm==curr_max:
                found_unique_max=False
            list_index-=1
        if found_unique_max==True:
            break
        prev_max = curr_max
        elem_index+=1 
    print('element_index',elem_index)
    print('1 returning',curr_max_index)
    return curr_max_index
#use=[[8,8,8,8,3,1,5],[8,8,8,8,8,2],[8,8,8,2,1],[8,8,8,8,8,8],[8,8,8,5],[8,8,8,8,8],[8,8,8,6],[]]
#print()
trails=int(input())
answer_list=[]
for x in range(trails):
    lent=int(input())
    data=input()
    data=data.split()
    numbers=[]
    for s in data:
        numbers.append(int(s))
    answer=[]
    times=0
    while numbers!=[] and times<1:
        times+=1
        use_list=[]
        # for s in numbers:
        #     use_list.append([s])
        # print(use_list)
        # max_index=find_max_index(use_list,lent)
        maximum=max(numbers)
        # print('max',maximum)
        # print('max_index',max_index)
        sub=[]
        sample=[]
        answer=[]
        use=False
        prev = None
        lenth_of_sub=0
        for a in numbers:
            if a==maximum:
                if (prev != maximum):
                    sample=[]
                    sub.append(sample)
                    lenth_of_sub+=1
                use=True
            if use==True:
                sample.append(a)
                prev = a
        print(sub)
        print(find_max_index(sub,lenth_of_sub,maximum))
        while sub!=[]:
            use_index=find_max_index(sub,lenth_of_sub,maximum)
            print("use_index", use_index)
            diff=len(sub)-use_index
            for h in range(diff):
                answer+=sub[use_index]
                sub.pop(use_index)
                lenth_of_sub-=1
        print(answer)
            
            
            
        
        

