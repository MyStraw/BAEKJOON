t, var = input().split()

def to_camel(words):
    return words[0] + ''.join(w.capitalize() for w in words[1:])

def to_snake(words):
    return '_'.join(w.lower() for w in words)

def to_pascal(words):
    return ''.join(w.capitalize() for w in words)

if t == '1':
    words = []
    start = 0
    for i, ch in enumerate(var):
        if ch.isupper():
            words.append(var[start:i].lower())
            start = i
    words.append(var[start:].lower())
elif t == '2':
    words = var.split('_')
elif t == '3':
    words = []
    start = 0
    for i, ch in enumerate(var):
        if ch.isupper() and i != 0:
            words.append(var[start:i].lower())
            start = i
    words.append(var[start:].lower())

print(to_camel(words))
print(to_snake(words))
print(to_pascal(words))
