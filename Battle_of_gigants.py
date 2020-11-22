a = int(input())
b = int(input())

if a > b:
    if (a - b) % 3 != 0:
        print('-1')
    else:
        ost = a % 3
        print((a - ost) // 3, ost_a, (b - ost) // 3)

else:
    if (b - a) % 3 != 0:
        print('-1')
    else:
        ost = a % 3
        print((a - ost) // 3, ost_a, (b - ost) // 3)
