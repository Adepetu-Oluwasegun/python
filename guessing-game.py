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