def bubble_sort(L):
    """Bubble sorting algorithm
    Complexity: O(n^2)
    
    Parameters: 
    L (list): list of numbers or strings 

    Returns:
    list: Sorted list

    """
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

def bubble_sort_effective(L):
    """Bubble sorting algorithm
    Complexity: O(n^2)
    
    Parameters: 
    L (list): list of numbers or strings 

    Returns:
    list: Sorted list

    """
    swapped = False
    while not swapped:
        swapped = True
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                swapped = False
    return L

print(bubble_sort([3,2,8,1,3,6,5]))

print(bubble_sort_effective([3,2,8,1,3,6,5]))
