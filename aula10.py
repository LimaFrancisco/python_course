# while

# i = 1

# while i < 10:
#     print(i)
#     i += 1

# print("finished")
# print(i)

# for

kids = ["Manu", "Vine", "Selina"]
#          0       1        2

# for item in kids: # item is a variable
#     print(item) # show every kids

# channel = "Refatorando"

# for letter in channel:
#     print(letter)

# for index in range(7, 90, 5): # start, finish and step 
#     print(index)


# for index in range(len(kids)):
#     print(kids[index], index)

# for index in range(5):
#     if index == 0:
#         print("first lines")
#     else:
#         print(f"other lines {index}")

matrix_numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in matrix_numbers:
    print("----")
    for column in row:
        print(column)