# Method 4: Optimization by √n
# Working
# In this method we’ll run the loop until the square root of the given number input as all the smallest factor of any number if any, lay in the interval [0, sqrt(number)]. Therefore, we’ll check for the factors within the above mentioned interval.
#
# For the given input integer we check for the following,
#
# If the number is divisible by  any number in the interval [2,sqrt(number)], if so then it’s not a prime.

num=7
flag=0
if num<2:
    flag=1
else:
    for i in range(2,int(pow(num,0.5)+1)):
        if num%i==0:
            flag=1
            break
if flag==1:
    print("Not prime number")
else:
    print("Prime Number")
    