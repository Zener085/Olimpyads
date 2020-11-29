def time_to_escape(n, m, r, c):
    min_n = r - 1
    max_n = n - r
    min_m = c - 1
    max_m = m - c

    return max(min_m, max_m) + max(min_n, max_n)

t = int(input())

for i in range(t):
    n, m, r, c = map(int, input().split())
    print(time_to_escape(n, m, r, c))
