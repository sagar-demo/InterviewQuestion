# For a user input num.
#
#  Initialize a variable sum = 0.
# Using a for loop in iteration ‘i’ iterate between [1, num].
# Each time add ‘i’ to current sum as sum = sum + i.
# Print sum.
# num = 5
# sum = 0
# for i in range(num+1):
#   sum+=i
# print(sum)

"""Using Formula for the sum of Nth Term"""
# num=5
# print(int(num*((num+1))/2))

"""Using Recursion Method  """
def recu(x):
  if x==0:
    return x
  return x+recu(x-1)
x=int(input("Enter a number"))
result=recu(x)
print(result)