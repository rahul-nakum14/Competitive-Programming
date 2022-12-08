#from array import *        # a = array('i',[10,20,30,40,50,60,70])
#import array as arr        # a = arr.array('i',[10,20,30,40])
#import array               # a = array.array('i',[10,20,30,40])

import array as arr

a = arr.array('i',[])
user_input = int(input("Enter size of array"))

for i in range (user_input):
    value = int(input("Enter Value"))
    a.insert(i,value)  #a.append(value)
    
search = int(input("Enter value to search"))

flag=0
for j in range(user_input):
            if a[j] == search:
                flag=1 
                # temp=j
                break
if flag == 1:
    print("value found at ",j)    
else:
    print("Not Found")
