# Method 3: Optimization by n/2 iterations
# Working
# In this method we’ll check if the number input have any factors within the range of 2 to number/2. Any number has it’s lowest factor after 1 if any, in the range[2,number/2].
#
# For a given integer input we check for the following,
#
# If the number input has factors in the range [2, number/2]. It’s not a Prime of the above condition is true.

num=19
flag=0
if num<2:
    flag=1
else:
    for i in range(2,int((num/2)+1)):
        if num%i==0:
            flag=1
if flag==1:
    print("Not prime number")
else:
    print("Prime number")