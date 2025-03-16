#libraries for system related changes
import sys

#sys.argv[] -- Command line arguments 
def main():
    print(sys.argv[0])

# set of a string gives a collection of unique characters
a = set("Hi Hi my name is Naman Naman")
# op - {'e', 'H', 's', 'N', 'n', 'y', 'i', ' ', 'a', 'm'}

# print(ls) -- gives error, list is mutable, therefore not hashable
# ls = {(0,1):"Hi", [2,3]:"Hello"}

# dir(sys) -- provides the methods associated with the object

#transposing of a matrix--using zip folder
matrix = [[1,2,3],[4,5,6],[7,8,9]]
trans = list(zip(*matrix))

#dunder / magic functions
class dunder_func:

    def __init__(self, name):
        # for initializaing an object
        self.name = name

    def __repr__(self):
        # for string representation of object
        return f'Person("{self.name}")'
     
    # ????????? -- What if for string we need another caller
    def __call__(self, x, y):
        # for calling an instance like a function
            return x + y
    
    def __getitem__(self, index):
        # for list indexing
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value
        # p = dunder_func([1,2,3])


# tuple packing
t = 12345, 54321, 'hello!'

#tuple unpacking
a,b,c = t

# tuples can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v[1].pop()
v[1].append(4) #output -- ([1, 2, 3], [3, 2, 4])

# enumerate used to for indexing
a = [1,2,3,4,5]
dictx=dict(enumerate(a))
# print(dictx)


#makes the file usable as a script as well as an importable module
# if __name__ == '__main__':
#     main()



import itertools
#count(start,step) -- infinte counting from start skipping the step
counter = itertools.count(10,2)
#cycle(data) -- infinite repetition of the data
cycler = itertools.cycle("ABC") # A,B,C,A,B,C
#repeat(data, repetitions) -- provides repitions of any data, if no repititions given it goes for infinte
acc = itertools.accumulate([1,2,3,4])
#product(data1,data2) -- produces cross product of the data given
prod = itertools.product((1,2),(3,4))
#similarly production of permutations and combinations take place
# for i in acc:
    # print(f"This is {i}")



import collections
#namedtuple used to provide named indexes to the elements of the datatype
P = collections.namedtuple('P',['x','y'])
a1 = P(11,12)


deq = collections.deque([1,2,3,4,5])
deq.append(7)
deq.appendleft(0)

#creates a dictionary for the number of unqiue characters available
countchar = collections.Counter("ABCABFDSVDTYFVSFSB")




#datetime
import datetime
# datetime.datetime.now() -- for date and time now
# datetime.date.today() -- date today

#custom date and time
custom_datetime = datetime.datetime(2024,12,24,10,30)
custom_date = datetime.date(2025,12,24)

#strftime -- formatting the datetime in any given format
formatted = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#convert the string into datetime object
date_string = "2024-12-25 10:30:00"
parsed_date = datetime.datetime.now().strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(parsed_date)  # Output: 2024-12-25 10:30:00

from datetime import timedelta

today = datetime.date.today()
tomorrow = today + timedelta(days=1)
# print(tomorrow)  # Output: 2025-02-11

past_date = today - timedelta(days=7)
# print(past_date)  # Output: 2025-02-03

import pytz

utc_time = datetime.datetime.now(pytz.utc)
# print(utc_time)  # Example: 2025-02-10 14:30:45.123456+00:00

# print(custom_date)


import os
# os.chdir('/home/naman/TTN_Bootcamp/Python/read_write')
# print(os.getcwd())
# print(os.listdir('/home/naman/TTN_Bootcamp/Python'))

# Create a new directory
new_dir = os.path.join(os.getcwd(), "example_dir")
# os.mkdir(new_dir)
# print("Created directory:", new_dir)

# Remove the directory (it must be empty)
# os.rmdir(new_dir)
# print("Removed directory:", new_dir)

# Rename a file (ensure the file exists)
# os.rename("old_filename.txt", "new_filename.txt")

# Remove a file (ensure the file exists)
# os.remove("new_filename.txt")

#to join submodules into a single path
path = os.path.join("folder", "subfolder", "file.txt")
# print("Joined Path:", path)

#os.path.exists(path) checks if a path exists.
# os.path.isfile(path) and os.path.isdir(path) check if a path is a file or directory.
# os.path.basename(path) and os.path.dirname(path)


# This will execute the command and print the output in the terminal
# os.system("echo 'Hello from the OS module!'")


# for root, dirs, files in os.walk(os.getcwd()):
#     print("Current Path:", root)
#     print("Directories:", dirs)
#     print("Files:", files)
#     break  # Remove break to traverse the entire tree

# print(os.getcwd())
# os.chdir('/home/naman/TTN_Bootcamp/Python')
# for key, value in os.environ.items():
#     print(f"{key}: {value}")

# print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"


import json
#json serialization -- creating JSON out of Python Object
data = {"name": "Alice", "age": 30, "city": "Wonderland"}
# Convert the dictionary to a JSON string
json_string = json.dumps(data, indent=4, sort_keys=True)
#deserialization -- loading the JSON into any python object
json_string_deser = json.loads(json_string)
print(json_string)
print(json_string_deser)


# function decorator
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decorator
def greet():
    print("Hello, World!")

# greet()

a = [1,2,3,4,5]
al = iter(a)
# print(next(al))
# print(next(al))



# class decorator
def election_age(fun):
    def wrapper(self):
        if self.age >= 18:
            fun(self)
    return wrapper

class Person:
    def __init__(self, age):
        self.age = age
    
    @election_age
    def vote(self):
        print("You can vote")
    

# p1 = Person(24)
# p1.vote()


# nums = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, nums))  # [1, 4, 9, 16, 25]
# evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# a, b = 5, 10
# a, b = b, a  # Now a=10, b=5



# a, b = 5, 10
# a, b = b, a  # Now a=10, b=5



# a = [1, 2, 3]
# b = a
# print(a is b)  # True (same object)
# print(a == b)  # True (same value)

# c = [1, 2, 3]
# print(a is c)  # False (different objects)
# print(a == c)  # True (same value)



'''
A metaclass is simply a class that inherits from type and overrides its behavior:
The type function can actually create classes dynamically:

MyDynamicClass = type("MyDynamicClass", (object,), {"x": 42})

obj = MyDynamicClass()
print(obj.x)  # Output: 42



Eg - 
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

# Output: Creating class MyClass

Explanation:

    MyMeta is a subclass of type, making it a metaclass.
    __new__() is called before the class is created.
    The MyClass class is created using MyMeta, so it triggers the metaclass's __new__() method
'''


# class Singleton:

#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,"instance"):
#             cls.instance = super().__new__(cls)
#         return cls.instance

# # Testing Singleton behavior
# obj1 = Singleton()
# obj2 = Singleton()

# print(obj1 is obj2)  # Output: True (Both are the same instance)
