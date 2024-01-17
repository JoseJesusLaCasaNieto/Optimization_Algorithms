# Algoritmo de ordenación por mezcla.
def mergesort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        lefthalf = lst[:mid]
        righthalf = lst[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                lst[k] = lefthalf[i]
                i += 1
            else:
                lst[k] = righthalf[j]
                j += 1
            k += 1
        
        while i < len(lefthalf):
            lst[k] = lefthalf[i]
            i += 1
            k += 1
        
        while j < len(righthalf):
            lst[k] = righthalf[j]
            j += 1
            k += 1
    
    return lst
    
lst = [5, 8, 4, 3, 9, 1]
print(mergesort(lst))

