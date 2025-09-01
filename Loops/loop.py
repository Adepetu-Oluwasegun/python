#CREATE LOOP
#while loop is a structure in python which allow us to loop through and execute a block of code multiple times
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

  i = 1
  while i <= 10:
    print(i)
    #i = i + 1
    i += 1 # shorthand

  print("Done with loop")

for letter in "kiddominant": # looping through each letter in the word
    print (letter)

acquaintances = ["jola", "folu", "titi", "tope"] 
for acquaintance in acquaintances:
  print(acquaintance)

for index in range(10):
  print(index)