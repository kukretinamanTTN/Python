def binary(num):
    return f"{num:b}"

def octal(num):
    return f"{num:o}"

def hexadecimal(num):
    return f"{num:x}"

num = int(input("Enter Number: "))
conv = int(input("Enter 1 for Binary, 2 for Octal, 3 for Hexadecimal: "))

if conv == 1:
    print(f"Binary Representation of {num} is " + binary(num))
elif conv == 2:
    print(f"Octal Representation of {num} is " + octal(num))
elif conv == 3:
    print(f"Hexadecimal Representation of {num} is " + hexadecimal(num))
else:
    print("Invalid!")