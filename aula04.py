my_string = "any text" # strings are anything written between quotation marks 

print(type(my_string)) # type of my_string 
print(my_string) # printing my_string valor

print(f"concatenate {my_string} in string") # best form to concatenate strings 

print(my_string.upper()) # turn everything uppercase
print(my_string.lower()) # turn everythin lowercase
print(my_string.capitalize()) # turn first letter uppercase

print(my_string.isupper()) # checks if the text is uppercase
print(my_string.islower()) # checks if the text is lowercase

print(my_string.strip()) # remove spaces at the beginning and end of a text
print(my_string.replace("any", "my")) # exchenge word and terms 

print(len(my_string)) # printing the lentgh of string
print(my_string[4]) # display the character referring to the value
print(my_string[2:5]) # display more then one character
print(my_string[-4:-1]) # backwards
print(my_string.index("text")) # printing the index of term 

# checking text in a substring
x = "text" in my_string
print(x) # return True or false
x = "tet" in my_string
print(x)

# string with many lines
my_string = """line 1,
line 2, 
line 3."""

print(my_string)

# string with many lins using scape character
my_string = "line 1,\nline 2,\nline 3."

print(my_string)

# The escape character is also used to write quotation marks in a string

my_string = "adding quotation marks \" in a string"
print(my_string)