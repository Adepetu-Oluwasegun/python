print(2)
print(2.9766)
print(-2.4454)
print(2 + 2.3 * 6)
print(2 * (9+2)) # do decide the order of execution for basic arithmetic

print(10 % 3) # to get the remainder of 10/3

my_num =7
print(my_num) # storing numbers inside of variable containers
print(str(my_num)) # converting my_num to string

print(str(my_num) + "my favorite number")

#functions that can be used with numbers
my_num = -5
print(abs(my_num)) # to get the absolute value

print(pow(3,2)) # raise 3 to the power of 2

print(max(4,6)) # to tell us the bigger number

print(min(4,6)) # to get the smallest number

print(round(23.66)) # to round up a number

# importing a python math; from external module giving us a lot of math functions
from math import *

my_num = -7
print(floor (3.7))
print(ceil(3.7))
print(sqrt(36))

try:  #try and except block helps handlle errors and do thing when they occur instead of throwing an error
  value = 10/0
  nomber = int(input("Enter a nomber: "))
  print(nomber)
except ZeroDivisionError as err: #best practice is to use it to capture specify errors 
  print("Divided by zero")
  print(err)
except ValueError:
  print("Invalid input")
