# Ashok Gangadharan 2018-02-06
# Collatz_conjecture: https://en.wikipedia.org/wiki/Collatz_conjecture

# User Input requested - no validations yet
m = int(input("Enter a Number : "))
n = m

while n >= 1:
    if n == 1:
        exit()
    elif n % 2 == 0:
        n = n / 2
        print(n)
    else:
        n = (n * 3) + 1
        print(n)
