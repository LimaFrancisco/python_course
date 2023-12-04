num1 = 5
num2 = 3.5

a = float(num1) # coverting for flaot 
b = int(num2)

print(type(a)) # printing data type

a = int(float("5.3")) # floating point string values cannot be converted to integer
b = "3.5"

print(type(a))

# arithmetic operators 
num1 + num2
num1 - num2 
num1 * num2
10 / 3
10 % 3
2 ** 3
10 // 3

(3 + 5 * 7 + 3)
((3 + 5) * (7 + 3))

# functions
print(abs(-15))
print(pow(3,3))
print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))
print(round(8.3))

import math # importing library 

print(math.floor(8.8))
print(math.ceil(8.1))
print(math.sqrt(9))