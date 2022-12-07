nums = [2,0,1]


for i in range(len(nums)):
    min = i
    for j in range(i+1,len(nums)):
        if nums[j] < nums[min]:
            min = j
    nums[i] , nums[min ] = nums[min],nums[i]

print(nums)