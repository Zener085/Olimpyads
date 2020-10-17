n, k = map(int, input().split())
a = []

x = input().split()

for i in range(n):
    a.append(int(x[i]))
    

while len(a) != k:
    a.sort()
    x, y = 0, 0
    if a[-1] % 2 == 0:
        x = a[-1] // 2
        y = x
    else:
        x = (a[-1] + 1) // 2
        y = x - 1
    a.pop(len(a) - 1)
    a.append(x)
    a.append(y)

a.sort()
x = 0
for i in a:
    x += i ** 2

print(x)
