x = int(input("x = "))
op = input("(+,-,*,/)")
y = int(input("y = "))
print(x, op, y)

if op == "+":
    print(x, op, y, "=", x + y)
elif op == "-":
    print(x, op, y, "=", x - y)
elif op == "*":
    print(x, op, y, "=", x * y)
elif op == "/":
    print(x, op, y, "=", x / y)
else:
    print("not supported")
