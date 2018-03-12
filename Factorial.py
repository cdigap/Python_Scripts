# Ashok Gangadharan 2018-03-07

# script for Factorial using a Function

# function Definition...
def factorial(x):
    y = 1
    while x > 1:
        y = x * y
        x = x - 1
    return y

# Calling function for 5
fact = factorial(5)

print('Factorial of 5 is : ', fact ,'\n') 

# Calling function for 7
fact = factorial(7)

print('Factorial of 7 is : ', fact ,'\n') 

# Calling function for 10
fact = factorial(10)

print('Factorial of 10 is : ', fact,'\n') 


# Output ...

# Factorial of 5 is :  120

# Factorial of 7 is :  5040

# Factorial of 10 is :  3628800
