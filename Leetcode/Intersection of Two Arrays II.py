nums1 = [1,2,2,1]
nums2 = [2]
k = []
nums1  = sorted(nums1)
nums2 = sorted(nums2)
i = j = 0
while (i < len(nums1) and j<len(nums2)):
    if nums1[i] == nums2[j]:
        k.append(nums1[i])
        i += 1
        j += 1
    elif nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1
print(k)
