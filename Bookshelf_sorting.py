# It doesn't work like I want,
#Idk why
def position(p):    
    a = []
    for i in range(len(p)):
        x = p[i]- i
        a.append(min(x, len(p) - x))
    return str(max(a) + 1)


n, q = map(int, input().split())
p = list(map(int, input().split()))

text = position(p) + '\n'

for i in range(q):
    a, b = map(int, input().split())
    p[a - 1], p[b - 1] = p[b - 1], p[a - 1]
    text += position(p) + '\n'

print(text[:-1])
