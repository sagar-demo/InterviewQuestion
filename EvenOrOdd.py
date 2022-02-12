#1. Check Whether a Number is Even or Odd in C++/python
# x=int(input("Enter a no"))
# if x%2==0:
#     print("Even No!")
# else:
#     print("Odd No!")

#Using Ternay operators
# Ternary Operator Syntax Python
# ( True : Action ) if ( Condition ) else ( False : Action )

# num=17
#
# print("Even")if num%2==0 else print("Odd")

3.

def evenno(x):
    return not x&1
if __name__ == "__main__":
    x=int(input("Enter a number"))
    if evenno(x ):
        print("Even")
    else:
        print("Odd")