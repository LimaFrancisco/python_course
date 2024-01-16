# open("path","r") # open is a main function for working with files

# mode
# r - read
# a - append 
# w - write
# x - create file
# r+ - read + write

# file = open("aula12/teste3.txt", "x")

# manipulating file

# print(file.readable()) # checking if the file is can be read
# print(file.read()) # reading file

# print(file.readline()) # read for line
# print(file.readline())
# print(file.readline())
# print(file.readline())

# list = file.readlines() # inserting file data into a list

# print(list[3])

# file.write("Python\n") # adding data into the file

# file.close() # to close the file

# OBS
# "a" - adding data to a file
# "w" - arrive all data and write new data or create a new file

# file deletion

import os

# if os.path.exists("aula12/teste2.txt"): # check the existence of the file and returns True or False
#     os.remove("aula12/teste2.txt") # the file need be closed before
# else:
#     print("the file does not exist")

# how to remove a folder


if os.path.exists("aula12/new_folder"):
    os.rmdir("aula12/new_folder") # only remove if the folder is empty
else:
    print("the folder does not exist")
