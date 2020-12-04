from random import randrange as rnd

text = ''
i = 1

while len(text) < 9125:
    text += str(i)
    i += 1

print(text[:9125])
