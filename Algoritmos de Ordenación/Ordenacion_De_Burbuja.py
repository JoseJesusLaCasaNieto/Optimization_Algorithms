# Algoritmo de ordenación de burbuja.
def bubblesort(lst):
    for num in range(len(lst)-1, 0, -1):
        for i in range(num):
            if lst[i] > lst[i+1]:
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    
    return lst

lst = [5, 8, 4, 3, 9, 1]
print(bubblesort(lst))


