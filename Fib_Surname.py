# Ashok Gangadharan
# A program that displays Fibonacci numbers.

# Week 1 Exercise

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 12
ans = fib(x)
print("Fibonacci number", x, "is", ans)

# Week 1 exercise 
# My name is Ashok, so the first and last letter of my name (A + K = 1 + 11) gives the number  12. The 12th Fibonacci number is 144.
#


# Week 2 Exercise

# Ashok Gangadharan
# A program that displays Fibonacci numbers using people's names.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Gangadharan"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)


# My surname is Gangadharan
# The first letter G is number 71
# The last letter n is number 110
# Fibonacci number 181 is 30010821454963453907530667147829489881


# Ord() is a built in function in Python which returns an integer representing the Unicode code point of the given Unicode character.
