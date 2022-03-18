# Method 6: Basic Recursion technique
# Working
# In this method we use the concept of recursion, to know more about recursion check out recursion in python.
#
# For the given integer input we perform the following
#
# Declare a recursive function checkPrime() with base cases as follows
# if number == iter, return True.
# if number < 2, return False.
# if number % iter == 0, return False.
# Set the Recursive step call as checkPrime(number,iter+1).
num=15
def checkprime(num,iter=2):
    if num==iter:
        return True
    if num%iter==0:
        return False
    if num<2:
        return False
    return checkprime(num,iter+1)

if checkprime(num)==True:
    print("Prime")
else:
    print("Not Prime")