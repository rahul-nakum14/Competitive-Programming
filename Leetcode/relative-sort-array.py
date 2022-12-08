    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = []
        q = []
        for j in range(len(arr2)):
            for i in range(len(arr1)):
                search = arr2[j]
                if search == arr1[i]:
                    k.append(arr1[i])

        y = set(arr1)
        x = set(arr2)
        

        for i in arr1:
            if i not in arr2:
                q.append(i)
        
        q.sort()

        for i in q:
            k.append(i)
        return k
