input_string = input()
A, B, C, D = map(int, input_string.split())
result = abs((A+D) - (B+C))
print(result)