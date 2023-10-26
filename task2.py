
def check_is_numb() -> int:
    no_a = input("Please enter a number A: ")
    no_b = input("Please enter a number B: ")
    if no_a.isnumeric() and no_b.isnumeric():
        return int(no_a), int(no_b)
    else:
        raise ValueError("This is not a number")
    
def check_char() -> str:
    sign_action = input("Please enter a simbol for calculation action '*', '/', '+', '-': ")
    spec_char = ["*", "/", "+", "-"]
    if sign_action in spec_char: 
        return sign_action
    else:
        raise ValueError("Bad sign")

def calculator(A: int, B: int, C: str) -> float:
    if C == "+":
        return float(A+B)
    elif C == "-":
        return float(A-B)    
    elif C == "*":
        return float(A*B)
    elif C == "/" and B != 0:
        return float(A/B)
    else:
        raise ZeroDivisionError("You can't divide from 0")

# print(calculator(*check_is_numb(), check_char()))

try:
    calculator(*check_is_numb(), check_char())
except ValueError:
    print(f"Bad simbol!")
except ZeroDivisionError:
    print("You can't divide from 0 chabe B to something else")
finally:
    print("Good bye!")

# print(calculator(*check_is_numb(), check_char()))