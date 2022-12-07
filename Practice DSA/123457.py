def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = []
        
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                k.append(left[i])
                i += 1
            else:
                 k.append(right[j])
                 j +=1

        k.extend(left[i:])
        k.extend(right[j:])

myList = [54,26,93,17,77,31,44,55,20]
mergeSort(myList)
print(myList)