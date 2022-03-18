# simple iterative solution
# in this method we,will use simple if-else statement and for loop to iterate through all the number
# in a given range while checking for factors of the numbers
#     for a given integer input we check
#     -if the number is greater than 2
#     -if the number has any factor in the range[2,number]
#     -if any off the above conditions are satisfied,the number is not prime number
n=11
flag=0
for i in range(2,n+1):
    if n%i==0:
        flag=1
        break
if flag==1:
    print("Not a prime number")
else:
    print("Prime Number")


