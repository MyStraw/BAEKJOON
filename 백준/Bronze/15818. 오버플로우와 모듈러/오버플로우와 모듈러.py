def multiply_modulo(numbers, M):
    result = 1
    for num in numbers:
        result = (result * num) % M
    return result

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

print(multiply_modulo(numbers, M))
