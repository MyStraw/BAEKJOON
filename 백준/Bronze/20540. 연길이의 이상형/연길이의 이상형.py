s = input().strip()

opposite = {
    'E': 'I', 'I': 'E',
    'S': 'N', 'N': 'S',
    'T': 'F', 'F': 'T',
    'J': 'P', 'P': 'J'
}

result = ''.join(opposite[ch] for ch in s)
print(result)
