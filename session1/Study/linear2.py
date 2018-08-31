items = [1,2,3,4,5,6,7,8,9]
x = int(input("enter a number:"))
if x in items:
    print("found")
    found_index = items.index(x)
    print("vi tri thứ:",found_index)
else:
    print("not found")
