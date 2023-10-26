#  Write a Python program that prompts the user to input an integer and raises
# a ValueError exception if the input is not a valid integer.

# exception ValueError:

# Raised when an operation or function receives an argument that has the right
# type but an inappropriate value, and the situation is not described by a more
# precise exception such as IndexError.

# Write a Python program that opens a file and handles a FileNotFoundError
# exception if the file does not exist. exception FileNotFoundError:

# number = input("Please enter number: ")
# try:
#     number.isnumeric()
#     print("Ok")
# except ValueError:
#     print("Is not number:")

from typing import Optional


def get_integer_input() -> Optional[int]:
    number = input("Please enter number: ")
    if number.isnumeric():
        return int(number)
    raise ValueError("Not number!")

try:
    print(get_integer_input())
except ValueError:
    print("Please enter number!")

def get_input_age() -> int:
    number = input("Enter your age: ")
    if number.isnumeric():
        if int(number) > 18:
            return int(number)
        else:
            raise ValueError("You are to young!")
    else:
        raise TypeError("Please enter number!")
    

try:
    age = get_input_age()
except ValueError:
    print("You are too young, you can't enter!")
except TypeError:
    print("Please enter number!")
else:
    print(age)
finally:
    print("I am done")

text = "Labas vakaras visiems"
text1 = []
text2 = ()
def split_to_list(in_tex: list):
    if type(in_tex) is not list:
        raise TypeError
    return len(in_tex())

try:
    print(split_to_list(text2))
except TypeError:
    print("This is not a list")

