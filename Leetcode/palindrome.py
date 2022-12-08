x = 454
num = x
rev=0
while x>0:
    last_digit = x%10
    rev = (rev*10)+last_digit
    x = x // 10
   
if num == rev:
    print("palindrome")
else:
    print("not palindrome")
