# Ashok Gangadharan 2018-02-18

#https://projecteuler.net/problem=5

# Number initializatoin
n = 0
i = 1

# While loop...
while n==0:
    # Incrementing i 
    i=i+1 
    # Checking if the number is divisible by a 1 to 20
    if  i%1==0 and i%2==0 and i%3==0 and i%4==0 and \
        i%5==0 and i%6==0 and i%7==0 and i%8==0 and \
        i%9==0 and i%10==0 \
        and \
        i%11==0 and i%12==0 and i%13==0 and i%14==0 and \
        i%15==0 and i%16==0 and i%17==0 and i%18==0 and \
        i%19==0 and i%20==0:
        # Once we get the result making sure we are off the while loop
        n=1
print("Smallest positive number that is evenly divisible by all of the numbers from 1 to 20: ", i)


# Smallest positive number that is evenly divisible by all of the numbers from 1 to 20:  232792560
