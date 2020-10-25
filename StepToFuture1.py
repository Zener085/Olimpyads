n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

x = int(input())
min_ost = x

for i in range(len(a)):
    if x - (a[i] % x) < min_ost:
        min_ost = x - (a[i] % x)
        count = i + 1
    print(x - (a[i] % x))

print(count, min_ost)
        
