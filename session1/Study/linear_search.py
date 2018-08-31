items = [6,3,7,4,9,0,1]
x = int(input("enter a number:"))


for index, item in enumerate (items):
    if x == items:        
        print("found it")
        print(index)
        break     
        
else:
    print("not found")
    

