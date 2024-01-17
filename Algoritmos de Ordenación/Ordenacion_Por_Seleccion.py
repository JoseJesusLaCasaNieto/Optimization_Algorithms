# Algoritmo de ordenación por selección.
def selectsort(lst):
    for index_1 in range(len(lst)-1, 0, -1):
        max_pos = 0
        for index_2 in range(1, index_1+1):
            if lst[index_2] > lst[max_pos]:
                max_pos = index_2
        temp = lst[index_1]
        lst[index_1] = lst[max_pos]
        lst[max_pos] = temp
    
    return lst

lst = [5, 8, 4, 3, 9, 1]
print(selectsort(lst))

