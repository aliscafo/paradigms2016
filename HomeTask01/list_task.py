# Remove equal adjacent elements
#
# Example input: [1, 2, 2, 3]
# Example output: [1, 2, 3]
def remove_adjacent(lst):
    new_lst = []
    
    if len(lst) != 0:
        new_lst.append(lst[0])
    
    for i in range(1, len(lst)): 
        if lst[i] != lst[i - 1]:
            new_lst.append(lst[i])
    
    return new_lst

 
# Merge two sorted lists in one sorted list in linear time
#
# Example input: [2, 4, 6], [1, 3, 5]
# Example output: [1, 2, 3, 4, 5, 6]
def linear_merge(lst1, lst2):
    merge_lst = []    
    i, j = 0, 0    
    n, m = len(lst1), len(lst2)
    lst1.append(float('inf'))
    lst2.append(float('inf'))
    
    while i < n or j < m:
        if i < n and lst1[i] <= lst2[j]:
            merge_lst.append(lst1[i])
            i += 1
        elif j < m and lst1[i] > lst2[j]:
            merge_lst.append(lst2[j])
            j += 1
    
    return merge_lst