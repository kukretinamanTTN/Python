# # result = 10 / 0
# name = 'naman'
# try:
# 	if name == int('naman')
# 	    print("Naman found")
# except SyntaxException as e:
# 	print("There is a syntax error:",e)

class NegativeException(Exception):
    pass

def is_even(x):
        if x < 0: raise NegativeException("Negative integer not allowed")
        return x % 2 == 0

try:
    print(is_even(0))
except NegativeException as e:
    print("This is a NegativeExeption: ",e)