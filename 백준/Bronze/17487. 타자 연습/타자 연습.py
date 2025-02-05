def count_keystrokes(s):
    left_keys = {'q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b', 'y'}
    left, right, other = 0, 0, 0

    for char in s:
        if char == ' ':
            other += 1
        elif char.isupper():
            other += 1
            if char.lower() in left_keys:
                left += 1
            else:
                right += 1
        else:
            if char in left_keys:
                left += 1
            else:
                right += 1

    while other > 0:
        if left <= right:
            left += 1
        else:
            right += 1
        other -= 1

    print(left, right)

s = input().strip()
count_keystrokes(s)