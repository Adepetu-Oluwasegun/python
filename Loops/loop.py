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