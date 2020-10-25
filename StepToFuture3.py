n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(input())

for i in range(n - 1, -1, -1):
    print(a[i][::-1] + a[i])

for i in range(n):
    print(a[i][::-1] + a[i])
