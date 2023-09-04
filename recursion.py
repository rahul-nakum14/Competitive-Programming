'''PRINT NO. FROM 1 TO N'''
# count = 0

# def recursion(n):

#     global count

#     if count >=n:
#         return
#     print(count)
#     count += 1
#     recursion(n)

# n = 5
# recursion(n)


'''PRINT NAME 1 TO N TIMES'''

# def name(i,n):
#     if i>n:
#         return
#     print("Rahul")
#     name(i+1,n)

# name(1,5)


'''PRINT NO. FROM 1 TO N (WITH A LITTLE CHANGED)'''
# def noprint(i,n):
#     if i>n:
#         return
#     print(i)
#     noprint(i+1,n)

# noprint(1,5)


'''PRINT NO. FROM N TO 1 (WITH A LITTLE CHANGED)'''
# def noprint(i,n):
#     if i<n:
#         return
#     print(i)
#     noprint(i-1,n)

# noprint(5,1)


'''PRINT NO. FROM 1 TO N (DON'T USE i+1)'''

# def print1ton(i,n):

#     if i<1:
#         return
#     print1ton(i-1,n)
#     print(i)

# print1ton(5,5)

'''PRINT NO. FROM N TO 1 (DON'T USE i-1)'''

# def printnto1(i,n):

#     if i>n:
#         return
#     printnto1(i+1,n)
#     print(i)

# printnto1(1,5)
 
'''SUM OF 1 TO N NO. (PARAMETERIZED)'''

# def sum1ton(i,sum):

#     if i<1:
#         print(sum)
#         return
#     sum1ton(i-1,sum+i)

# sum1ton(5,0)



'''SUM OF 1 TO N NO. (FUNCTIONAL)'''

# def sum1ton(n):

#     if n == 0:
#         return 0
    
#     return n + sum1ton(n-1)

# print(sum1ton(5))



'''FACTORIAL OF 1 TO N NO. (FUNCTIONAL)'''

# def fact(n):

#     if n == 0:
#         return 1
    
#     return n * fact(n-1)

# print(fact(5))

'''PALINDROME ARRAY'''

#   MY APPROACH
# def palindrome(arr,first,last):

#     if first >=len(arr) or arr[first] != arr[last]:
#         return False
    
#     first +=1
#     last -=1

#     palindrome(arr,first,last)
#     return True



# arr = [1,2,3,2,1,5]
# first = 0
# last = len(arr)-1

# print(palindrome(arr,first,last))

'''PALINDROME ARRAY Striver '''
def palindrome(i,arr):

   if i >= len(arr)//2:
      return True
   
   if arr[i] != arr[len(arr)-i-1]:
      return False
   
   return palindrome(i+1,arr)

arr = [1,2,3,2,1]
print(palindrome(0,arr))
