n = int(input())
a = list(map(int, input().split()))
mx = max(a)
a.append(mx)
res = 0
for i in range(0, n):
    if a[i] < a[i+1]:
        res += a[i + 1] - a[i]
print(res)
