

# Задача 1
def example():
    value = (5 + 7*5/8) / 3**5
    return print(round(value, 2))

example()

#############################################################
# Задача 2
def breakpoint(v: int, t: int):
    point_to_stop = v*t
    if point_to_stop > 109:
        point_to_stop -= 109
    return print(point_to_stop)

breakpoint(30, 5)

# v = int(input())
# t = int(input())
############################################################
# Задача 3
def greatest_number(x: float, y: float):
    if x>y:
        print(x)
    else:
        print(y)

greatest_number(-12.2, -2)

######################################

# Часть2
# Задача 1
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

# Задача 2
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 and y1 != y2:
    print('YES')
elif y1 == y2 and x1 != x2:
    print('YES')
else:
    print('NO')
