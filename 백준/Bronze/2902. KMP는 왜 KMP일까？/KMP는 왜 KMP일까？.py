s = input()

parts = s.split('-')
result = ''.join(part[0] for part in parts)

print(result)