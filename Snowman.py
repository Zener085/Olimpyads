s = input()
n = int(input())
a = []
for i in s:
    a.append(ord(i))

x = min(a)
s = [x]
y = a.index(x)
for i in range(n - 1):
    if a[y - 1] == a[y + 1]:
        if a[y - 2] > a[y + 2]:
            x = a[y + 1]
        else:
            x = a[y - 1]
    else:
        x = min(a[y - 1], a[y + 1])
    s.append(x)
    y = a.index(x)

text = ''
for i in s:
    text += str(chr(i))
print(text)
