def is_inside(point, rectangle):
    [x1, y1] = point
    [x2, y2, width, height] = rectangle
    test1 = x2 <= x1 <= (x2 + width)
    test2 = y2 <= y2 <= (y2 + height)

    if test1 and test2:
        return True
    else:
        return False

point = [200,120]
rectangle = [140, 60, 100, 200]
if is_inside(point, rectangle):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")