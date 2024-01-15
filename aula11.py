try:
    num = int(input("enter a number: "))
    print(num)

    # 10 / 0

except ZeroDivisionError: # error division by zero
    print("division by zero is not possible")

except ValueError: # error invalid value
    print("enter a valid value")

except: # for any unexpected error 
    print("unexpected error")

finally:
    print("aways performs")