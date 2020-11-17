def weight(i):
    k = 0
    while i % 2 == 0 and i != 0:
        k += 1
        i //= 2
    return k ** 2 + k + 1

def find_n():
    summary = 0
    for i in range(1, 100000):
        if i % 2 == 0:
            summary += weight(i)
            print(weight(i))
            

        if summary >= 1000:
            print(i)
            break
