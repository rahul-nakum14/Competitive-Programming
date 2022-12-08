#Bruteforce Method
import array as arr

a = arr.array('i',[2,7,11,15])

sum=0
target=9
def twosum():
    for i in range(len(a)):
        for j in range(i+1,len(a)):
                sum=a[i]+a[j]
                if sum == target:
                    return[i,j]
x = twosum()
print(x)

'''Output [0, 1]'''

#Hashmap Method

import array as arr
a = arr.array('i',[3,2,4])
hashmap = {}

def hash():
    targt=6
    for i in range(len(a)):
        comp = targt - a[i]
        if comp in hashmap:
            return[hashmap.get(comp),i]    # return[hashmap[comp],i] get values from key
        else:
            hashmap[a[i]] = i              # Value , index
print(hash())

'''Output [1, 2]'''

''' leet code submission
        for i in range (len(nums)):
            com = target - nums[i]
            if com in hashmap:
                return[hashmap.get(com),i]
            else:
                hashmap[nums[i]] = i '''
