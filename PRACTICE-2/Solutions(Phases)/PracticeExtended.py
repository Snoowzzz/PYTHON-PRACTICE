##### Extend pracitce for overall topics 
### Questions included in phase 6 questions
### Question 1 
# Input:  [3, 1, 4, 1, 5, 9, 2, 6]
# Output: [1, 3, 1, 4, 2, 9, 5, 6]  ← many valid answers exist
def zigzag(lst):
    lst.sort()
    k = len(lst)
    if len(lst) % 2 == 0:
        lsta = lst[:int(k/2)]
        lstb = lst[int(k/2) :]
    else:
        t = (k+1)/2
        lsta = lst[:int(t)]
        lstb = lst[int(t):]
    finallst = []
    for i in range(len(lstb)):
        finallst.append(lsta[i])
        finallst.append(lstb[i])
    finallst.append(lsta[-1])
    return finallst
lst = [3, 1, 4, 1, 5, 9, 2]   
print(zigzag(lst))    
        
        