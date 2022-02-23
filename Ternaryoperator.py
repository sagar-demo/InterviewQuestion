#Find the Greatest of the Three Numbers in Python Language
# Method 3: Using Ternary Operator
# In this method we use Ternary operator to compare and find the Largest Number among the three integer inputs.
#
# Working
# For integer inputs number1, number2 and number3
#
# Initialize the required variables.
# Using Ternary Operator check if the numbers are greater than max and change max if true.
# Print max variable.
# Let’s implement the working in Python Language.

first=10
second=20
third=40
greatest=(first if first>second else second)
greatest=(third if third>greatest else greatest)
print(greatest)