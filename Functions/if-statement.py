#
is_male = True

if is_male:
  print("You are a man")
else:
  print("you are not a man")

is_female = False

if is_female:
  print("you are not a woman")
else:
  print("you are a woman")

is_tall = True
is_playful = True

if is_tall or is_playful:
  print("he is tall and playful")

is_male = True
is_tall = False

if is_male and is_tall:
  print("you are a tall man")
  
elif is_male and not(is_tall):
  print("you are a short man")

elif not is_male and (is_tall):
  print("you are not a man but you are tall")

else:
  print("you are either a man or tall")