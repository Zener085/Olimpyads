# It's doesn't work
# It can't do it, it's creation of hell
n = int(input())
a = []
list_m = []

for i in range(n):
    m = int(input())
    for k in range(m):
        s = True
        w, c = map(int, input().split())
        for j in range(len(a)):
            if int(w) == a[j][0]:
                a[j][1] += c
                s = False
                break
        for j in range(len(a) - k):
            if a[j][0] > w:
                if len(a[j]) == 3:
                    if a[j][2] < c:
                        a[j][1] += c - a[j][2]
                        a[j][2] = c
                else:
                    a[j].append(c)
                    a[j][1] += c
        if s:
            a.append([w, c])
            for j in range(len(list_m)):
                if j == 0:
                    for h in range(list_m[j]):
                        if a[-1][0] > a[h][0]:
                            if len(a[-1]) == 3:
                                if a[-1][2] < a[h][1]:
                                    a[-1][1] += a[h][1] - a[-1][2]
                                    a[-1][2] = a[h][1]
                            else:
                                a[-1][1] += a[h][1]
                                a[-1].append(a[h][-1])
                else:
                    for h in range(list_m[j - 1], list_m[j] + list_m[j - 1]):
                        if a[-1][0] > a[h][0]:
                            if len(a[-1]) == 3:
                                if a[-1][2] < a[h][1]:
                                    a[-1][1] += a[h][1] - a[-1][2]
                                    a[-1][2] = a[h][1]
                                else:
                                    a[-1][1] += a[h][1]
                                    a[-1].append(a[h][-1])
    list_m.append(m)

q = int(input())
z = list(map(int, input().split()))
text = ''
for x in z:
    min_f = None
    
    for f in range(len(a)):
        if a[f][1] >= x:
            if min_f == None or a[f][0] < min_f:
                min_f = a[f][0]
    
    if min_f == None:
        text += '-1 '
    else:
        text += str(min_f) + ' '
print(text[:-1])
