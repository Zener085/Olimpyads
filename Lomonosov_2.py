N = int(input()) 
if N % 2 == 0:
    res = 2 ** ((( N // 2) ** 2))
    print(res)
else:
    print('0')
