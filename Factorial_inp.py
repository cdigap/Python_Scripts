# Ashok Gangadharan 2018-03-18

# script for Factorial using a Function and taking input from the user

# function Definition...
def factorial(x):
    y = 1
    while x > 1:
        y = x * y
        x = x - 1
    return y

x = int(input("Enter a Number : "))

# Calling function for x
fact = factorial(x)

print('Factorial of',x,'is : ', fact ,'\n') 



# Enter a Number : 10
# Factorial of 10 is :  3628800 
