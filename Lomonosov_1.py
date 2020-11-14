D = str(input())
L = int(input())
N = input()

s16 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
       '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010',
       'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

s8 = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5',
      '110': '6', '111': '7'}

M = ''

for i in range(L):
    M += s16[N[i]]

if '1' in M:
    while M[:3] == '000':
        M = M[1:]
    M = M[3 - (len(M) % 3) - 1:]
    if len(M) % 3 == 1:
        M = '00' + M
    elif len(M) % 3 == 2:
        M = '0' + M
else:
    M = '000'

N = ''
a = []

if len(M) % 3 == 0:
    for i in range(len(M) - 3, -1, -3):
        a.append(M[i: i + 3])

else:
    for i in range(len(M) - 3, len(M) % 3 - 1, -3):
        a.append(M[i: i + 3])
    a.append(M[:len(M) % 3])

for i in range(len(a) - 1, -1, -1):
    N += s8[a[i]]

count = 0
for i in N:
    if i == D:
        count += 1
print(count)
