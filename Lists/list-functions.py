# different functions we can use with lists to make them more powerful and make them more easy to use
lucky_numbers = [4, 8, 12, 16, 20]
friends = ["Rajeesh koothrapali", "Ogbono Merchant", "poseidon", "Richmonk", "Basic Bitch"]

print(friends)

friends.append("basic bitch") # add new elements to a list


friends.insert(1, "shinpachi")

print(friends)

friends.remove("shinpachi")

print(friends.index("Ogbono Merchant"))

friends.sort()

print(friends)

lucky_numbers.sort()

print(lucky_numbers)

friends2 = friends.copy()
print (friends2)

friends.extend (lucky_numbers)
print(friends) # extend function is to add two lists together
