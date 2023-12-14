def big_mac(): # for start a function ,aways use def 
    print("sandwich big mac")

#print("start")
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#big_mac()
#print("end")

def make_big_mac(name):
    print(f"sandwich big mac {name}")

#make_big_mac("Roger")
#make_big_mac("Cris")
#make_big_mac("Manu")
    
def make_fries(size):
    print(f"fries {size}")

def prepare_soda(type, size):
    print(f"{type} {size}")

#make_big_mac("Roger")
#make_fries("Medium")
#prepare_soda("Coca", "big")

def meke_combo_big_mac(name, size, type, size_soda):

    make_big_mac(name)
    make_fries(size)
    prepare_soda(type, size_soda)

#meke_combo_big_mac("Roger", "Big", "Fanta", "Medium")
       
def sum_numbers(num1, num2):
    return num1 + num2

result = sum_numbers(25, 15)

#print(result)

def largest_number(list_num):
    list_num.sort()
    list_num.reverse()
    largest = list_num[0]
    return largest

list_num = [1, 654, 232, -34, -87, -1231, 675]

num = largest_number(list_num)

print(num)