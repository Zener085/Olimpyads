n = int(input())
a = int(input())
x = int(input())
m = int(input())

v = 0

for i in range((n * a - x) // m):
    v += 1
print(v)
