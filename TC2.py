n = input()
while '(' in n:
    n = n[1:-1]
    a = 0
    qount = 0
    for i in n:
        try:
            i = int(i)
            a = a * 10 + i
            qount += 1
        except:
            break
    n = n[qount:]
    print(n)
    
