 # FUNCTIONS: a collection of code which performs  specific tasks
def say_hi(name, age):
  print("Hello " + name + ", you are " + age)

say_hi("Rajeesh Koothrappali", "50")

def print_sway():
    text = "sway has a good neck"
    print(text)
    print(text)
    print(text)
    print_sway()

def print_kiddo(text):
  print(text)
  print(text)
  print(text)

print_kiddo("kiddo is a trouble maker")

# usinf a If statement in betweeen a function
def school_age_calculator(age,name):
  if age < 5:
    print("Enjoy the time!", name, "is only", age,)
  elif age == 5:
    print("Enjoy kindergarten,", name)
  else:
    print("they grow up so fast!")
school_age_calculator(6,"sway")

# how to get a value back from a function
def add_ten_to_age(age):
  new_age = age + 10
  return new_age

How_Old_Will_I_Be = add_ten_to_age(3)
print(How_Old_Will_I_Be)