# a dictionary is a special structure which allows us to store informations in what are called key value pairs. i can create a bunch of key value pairs and when i want to access a piece of information from the dictionary i can refer to the key value pairs. dicitonaries are created in a {}

# creating a program which allow us to convert a month name to a 3 letter name

monthConvertions = {
  #keys   values
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December",
}

print(monthConvertions["Nov"])
print(monthConvertions.get("Dec"))
