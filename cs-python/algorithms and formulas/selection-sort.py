def selection_sort(L):
    """Selection sorting algorithm
    Complexity: O(n^2)
    
    Parameters: 
    L (list): list of numbers or strings 

    Returns:
    list: Sorted list

    """
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L

print(selection_sort([3,2,8,1,3,6,5]))
