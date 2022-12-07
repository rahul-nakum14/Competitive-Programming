a = [1,2,3,4,5,6,7]
k= 3
b = []

for i in range (len(a)):
    b.append(a[i],3)
print(b)

# print(a[-1:])
#  
        # for i in range(0, k):
        #     num = nums.pop()
        #     nums.insert(0, num)
# while k:

#     a[:] = a[-1:] + a[:-1]
#     print(a)
#     k -= 1
#     if k<=0:
#         break


    # class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     while k:
    #         nums[:] = nums[-1:] + nums[:-1]
    #         k -= 1
    #         if k<=0:
    #             break