direction = 0
commands = [int(input()) for _ in range(10)]
for cmd in commands:
    if cmd == 1:
        direction = (direction + 1) % 4
    elif cmd == 2:
        direction = (direction + 2) % 4
    elif cmd == 3:
        direction = (direction - 1) % 4
final_direction = ['N', 'E', 'S', 'W'][direction]
print(final_direction)