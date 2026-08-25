##### Extend pracitce for overall topics 
### Questions included in phase 6 questions
### Question 1 
# Input:  [3, 1, 4, 1, 5, 9, 2]
# Output: [1, 3, 1, 4, 2, 9, 5, 6]  ← many valid answers exist
def zigzag(lst):
    newlst = lst.sort()
    k = len(lst)
    if len(lst) % 2 == 0:
        lsta = lst[:(k/2)]
        lstb = lst[k/2 :]
    else:
        
        