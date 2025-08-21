# Building a basic calculator where we get two numbers from a user and we add it together and print it to our screen
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result =int(num1) + int(num2)


#  building advance calculator

nom1 = float(input ("Enter the first number: "))
op = input("Enter operator: ")

nom2 = float(input ("Enter the second number: "))

if op == "+":
  print(nom1 + nom2)
elif op == "-":
  print(nom1 - nom2)
elif op == "/":
  print(nom1 / nom2)
elif op == "*":
  print(nom1 * nom2)
else:
  print("invalid operator")
