secret_word = "Elephant"
guess = ""
guess_count = 0 # number of guesses
guess_limit = 3 # guess in 3 tries
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):  # while guess is not eqal to secret word and you are not out of guesses
  if guess_count < guess_limit: # if guess count is less than guess limit
    guess = input("Enter guess: ")
    guess_count +=1

  else:
    out_of_guesses = True

if out_of_guesses:
    print("you are out of guesses, you Lose!")
else:
    print ("you win!")

import random 

random_number = random.randint (1, 20)

print("i am thinking of a number")

attempts = 0
guess = 0

while guess != random_number:
  guess = int(input("Take a guess: "))
  attempts +=1
if guess < random_number:
  print("Too low! Try again")
if guess > random_number:
  print("Too high! Try again")
elif guess == random_number:
  print(f"congratualations you guess right in  {attempts} attempts")


sentence = input("input a sentence: ")
words = sentence.split()
print(len(words))

new_number = int(input("Enter a number: "))

if new_number % 2 == 0:
  print(str(new_number) + " is a even number ")
else:
  print(str(new_number) + " is a odd number ")


n = int(input("Enter a number: "))
result = 1

for i in range(1, n + 1):
  result = result * i

print("The factorial number of " + str(n) + " is " + str(result))

d = int(input("Enter a number: "))
for i in range(1, 13):
  result = d * i
  print(str(n) + " x " + str(i) + " = " + str(result))

g = input("Enter a number: ")
total = 0

for digit in g:
  total = total + int(digit)
  print("The sum of digit is " + str(total))