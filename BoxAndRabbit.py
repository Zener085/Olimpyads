def move_y(y1, y2):
    t_y = 0
    
    if y1 < y2:
        t_y += y2 - y1
    else:
        t_y += y1 - y2
    if t_y < 0:
        t_y *= (-1)
    
    return t_y
    print(t_y)

def move_x(x1, x2, y1, y2):
    t_x = 0
    if x1 < x2:
        t_x += x2 - x1
    else:
        t_x += x1 - x2
    if t_x < 0:
        t_x *= (-1)

    if y1 != y2:
        t1 = move_y(y1, y2)
        return t_x + t1 + 2
    else:
        return t_x

x = int(input())
for i in range(x):
    x1, y1, x2, y2 = map(int, input().split())
    t = 0

    if x1 != x2:
        t = move_x(x1, x2, y1, y2)
    else:
        if y1 != y2:
            t = move_y(y1, y2)

    print(t)
