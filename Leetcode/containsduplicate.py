class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set()
        for i in nums:
            if i in a :
                return True
            a.add(i)
        return False



nums = [-5,9,5]
a = []
flag=0
for i in nums:
        if i in a :
            flag=1
        a.append(i)
if flag == 1:
    print("true")
else:
    print("false")
