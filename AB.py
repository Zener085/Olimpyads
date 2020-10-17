def BB(stroke):
    return stroke.replace('BB', '', 1)

def AB(stroke):
    return stroke.replace('AB', '')

t = int(input())
for i in range(t):
    text = input()
    text_check = ''

    while text_check != text:
        text_check = text
        if text == AB(text):
            text = BB(text)
        else:
            text = AB(text)

    print(len(text))
