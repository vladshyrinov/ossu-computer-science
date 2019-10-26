def mergeSort(L):
    
    def mergeHelper(left, right):
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result 

    if len(L) < 2:
        return L[:]
    else:
        mid = len(L) // 2
        left = mergeSort(L[:mid])
        right = mergeSort(L[mid:])
        return mergeHelper(left, right)

print(mergeSort([]))
print(mergeSort([1]))
print(mergeSort([2,1,4,5,3,5,6,2,9]))
