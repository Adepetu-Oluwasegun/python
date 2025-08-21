# a dictionary is a special structure which allows us to store informations in what are called key value pairs. i can create a bunch of key value pairs and when i want to access a piece of information from the dictionary i can refer to the key value pairs. dicitonaries are created in a {}

# creating a program which allow us to convert a month name to a 3 letter name

monthConversions = {
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

print(monthConversions["Jan"])
print(monthConversions.get("Feb"))
print(monthConversions.get("Mar"))
print(monthConversions.get("Apr"))
print(monthConversions.get("May"))
print(monthConversions.get("Jun"))
print(monthConversions.get("Jul"))
print(monthConversions.get("Aug"))
print(monthConversions.get("Sep"))
print(monthConversions.get("Oct"))
print(monthConversions.get("Nov"))
print(monthConversions.get("Dec"))

weekConversions = {
  "Sun": "Sunday",
  "Mon": "Monday",
  "Tue": "Tuesday",
  "Wed": "Wednesday",
  "Thu": "Thursday",
  "Fri": "Friday",
  "Sat": "Saturday"
}