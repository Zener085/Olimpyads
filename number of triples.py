def number_of_triples():
    q = 0
    for x in range(-1000, 1000):
        for y in range(x, 1000):
            for z in range(y, 1000):
                if (x + y + z == 3) and (x ** 3 + y ** 3 + z ** 3 == 24):
                    q += 1
    print(q)
