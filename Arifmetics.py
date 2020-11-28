a, b, c = map(int, input().split())

if a * b == c or a * c == b or b * c == a:
    print('Yes')
    x = [a, b, c]
    x.sort()
    if x[0] == 0:
        x[0], x[2] = x[2], x[0]
    print(*x)
else:
    print('No')
