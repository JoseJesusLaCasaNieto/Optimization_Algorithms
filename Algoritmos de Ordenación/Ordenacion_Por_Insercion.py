# Algoritmo de ordenación por inserción.
def sort_lst(lst):
    for position in range(len(lst)):
        value = lst[position]

        while position > 0 and lst[position - 1] > value:
            lst[position] = lst[position - 1]
            position = position - 1
        
        lst[position] = value
    
    return lst

lst = [5, 8, 4, 3, 9, 1]
print(sort_lst(lst))

