t = input()
if len(t) % 2 == 0:
    n = len(t) // 2
else:
    n = len(t) // 2 + 1
x = True

for i in range(1, n):
    if len(t) % 2 == 0:
        if t[n - i:] == t[:n + i]:
            print('YES')
            print(t[:n + i])
            x = False
            break
    else:
        if t[n - i:] == t[:n + i - 1]:
            print('YES')
            print(t[:n + i - 1])
            x = False
            break

if x:
    print('NO')
