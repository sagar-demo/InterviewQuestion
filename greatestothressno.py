#Program to find the Greatest of Three Numbers in python

# Methods discussed in the post –
# Method 1: Using simple if-else conditions
# Method 2: Using ternary operators
# Method 3: Using inbuilt max functions
# Method 1
# Algorithm
# For user inputs of numbers as first, second and third.
#
# Step 1: Check if first number is greater than second and third
# Print first is the greatest
# Step 2: Check if second number is greater than first and third
# Print second is the greatest
# Step 3: Third number has to be greatest

# Print third is the greatest

def greast(first,second,third):
    if first>=second & first>=third:
        print(first,"is the greatest")
    elif second>=first & second>=third:
        print(second,"is greatest")
    else:
        print(third,"is greatest")
 ## **User input** ###
# first=int(input("Enter the First value"))
# second=int(input("Enter the second value"))
# third=int(input("Enter the third value"))
greast(first=8,second=8,third=10)