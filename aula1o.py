# set and dictionary

# set - unordered list, does not accept duplicate value, data cannot be modifield, does not have index

# fruits = {"apple", "orange", "pineapple", "apple"} # declaration of set 

# fruits.add("pear") # adding 

# fruits.remove("apple") # removing

# fruits.pop() # removing a random value

# print(fruits)

# set1 = {0,3,50,74}
# set2 = {True, False, False, False}
# set3 = {"Roger", 34, True} # diferent data types

# print(set3)


# dictionary

month = {
    "jan" : "january",
    "feb" : "february",
    "mar" : "march",
    "apr" : "april",
    "may" : "may",
    "jun" : "june",
    "jul" : "july",
    "aug" : "august",
    "sep" : "september",
    "oct" : "october",
    "nov" : "november",
    "dec" : "december"
}

print(month["jan"])

print(month.get("abc", "standard")) # pattern for key not found

print(len(month))