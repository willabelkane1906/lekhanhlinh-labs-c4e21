# 1. generate expression
from random import randint, choice
from calc2 import calculate
x = randint(0, 9)
y = randint(0, 9)
op = choice(["+", "-", "*", "/"])
print(op)
error = randint(-1, 1)

r = calculate(x, y,op) + error
print( x,op, y, "=", r)
# 2. ask user
user_answer = input("(Y/N) ?").upper()

# 3. print result
if calculate(x,y, op) ==r:
    if user_answer == "Y":
        print("yay")
    elif user_answer == "N":
        print("nah")
else:
    if user_answer == "Y":
        print("nah")
    elif user_answer == "N":
        print("yay")