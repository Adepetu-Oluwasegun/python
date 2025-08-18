# print("Hello World")

# # operators
# print (4 + 4)
# print (2 + 2 * 5)
# print (2**5)
# print (5/2)
# print (5//2) # to get exact
# print (5%2) # to know the number of remainders

# # strings
# print("what's up")
# print ('whats up')

# # variable assign data to a variable they can hold different values, they are case sensitive and don't start with numbers.
# red_bucket = "kevin"
# print(red_bucket)

# # request input and assign it to a variable
# red_bucket = input("what do you what to put in the bucket? ")

# # conditional logic true/false
# # when you check for equality u use "=="
# print(5==4)
# print(5!=4) # != means not equal to

# #combining different operators with variables
# Thomas_Age = 5
# Age_at_kindergarten = 5

# #print(Thomas_Age == Age_at_kindergarten)
# if Thomas_Age < Age_at_kindergarten: print("Thomas should be in pre-school ")
# elif Thomas_Age == Age_at_kindergarten:
#   print("Enjoy kindergarten")
# else:
#   print("Thomas should be in another class")

  # FUNCTIONS: a block of code you can package together with a name and it does something anytime u print
def print_sway():
    text = "sway has a big dick"
    print(text)
    print(text)
    print(text)

#print_sway()

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

#CREATE LOOP
#while loop
x=0
while (x<5):
  print(x)
  x=x+1

#for loop
for x in range(5,10):
  print(x)

days=["mon", "tues", "weds", "thurs", "fri"]

for d in days:
  if (d=="thurs"):break
  print(d)

for d in days:
  if (d=="thurs"):continue
  print(d)

  #print out the value of pi from existing library. you can build untop what other people have done
import math
print("pi is", math.pi)

name = 'swaylee'
print("hello,", name)

first_name = "Oluwasegun"
last_name = "Adepetu"
middle_name = "Emmanuel"

print(first_name, middle_name, last_name)

def convert_kilogram_to_grams(kilograms):
  return kilograms * 1000

kg = convert_kilogram_to_grams(50)
print(kg)

# draw a triangle
print("   /\\" )
print("  /  \\" )
print(" /    \\")
print("/______\\")

# draw a square
print(" ______________")
print("|              |")
print("|              |")
print("|              |")
print("|              |")
print("|______________|")

name = "hijikata toshiro"
age = "23"
print(" My name is " + name + " and i am " + age + " years old")
print(" i am a student of computer science and at " + age + " i think i am doing well for my self")
print(" i don't like being reminded that i am young as a " + age + " years old japanese student")

name = "gintama"
age ="30"

print(" My name is " + name + " and i am " + age + " years old")
print(" i am a student of computer science and at " + age + " i think i am doing well for my self")
print(" i don't like being reminded that i am young as a " + age + " years old japanese student")

# datatypes
"hello, world" # this is a string for storing plain text 
50 # integers
is_Male = True # boolean value(store value of either true or false)

# use \n to create a new line into a string
print(" i am a student of computer science \n and at " + age + " i think i am doing well for my self")

# use \"a backslash" to escape a quotation
print(" i am a student of computer science and at " + age + " i think i \am doing well for my self")

# converting a string to upper case and lower case
phrase = " i need to speak"
print(phrase)
print(phrase.upper())
print(phrase.lower())

# get the length of a string 
print(len(phrase))

# how to grab individual character from a strong
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])
print(phrase[4])
print(phrase[5])
print(phrase[6])
print(phrase[7])
print(phrase[8])
print(phrase[9])
print(phrase[10])
print(phrase[11])
print(phrase[12])
print(phrase[13])
print(phrase[14])
print(phrase[15])

# how to grab or return index of a specific character
print(phrase.index(" "))
print(phrase.index("i"))
print(phrase.index(" "))
print(phrase.index("n"))
print(phrase.index("e"))
print(phrase.index("e"))
print(phrase.index("d"))
print(phrase.index(" "))
print(phrase.index("t"))
print(phrase.index("o"))
print(phrase.index(" "))
print(phrase.index("s"))
print(phrase.index("p"))
print(phrase.index("e"))
print(phrase.index("a"))
print(phrase.index("k"))

# how to replace certain text or characters in a string
print(phrase.replace("need", "want"))

# working with numbers
