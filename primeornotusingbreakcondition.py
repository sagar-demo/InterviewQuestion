# Method 2: Optimization by break condition
# Working
# In this method we’ll check if the number is divisible by any other number except the number itself and 1. We eliminate the possibilities using if-else statements.
#
# For a given integer input, we check for the following
#
# If number is smaller than 2.
# If the number has any other factors besides itself and 1.
# If any other the conditions are satisfied, the number is not a Prime.

num=43
flag=0
if num<2:
    flag=1
else:
    for i in range(2,num+1):
        if num%i==0:
            flag=1
            break
    if flag==1:
        print("Not a prime number!")
    else:
        print("Prime number!")