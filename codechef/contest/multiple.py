num1 = int(input("ENTER FIRST NUMBER : "))
num2 = int(input("ENTER SECOND NUMBER : "))
divisor = 0
print("THE COMMON DIVISORS OF NUMBER ",num1," AND ",num2," ARE -")
for i in range(1,min(num1,num2)+1):
  if num1%i == num2%i == 0:
    divisor = i
    if divisor:
        print("True")
    else:
        print("False")