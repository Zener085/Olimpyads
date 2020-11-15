def x(n):
    n = n ** 11 - n
    a = []
    
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)
        if i > 66:
            break
    print(*a)
