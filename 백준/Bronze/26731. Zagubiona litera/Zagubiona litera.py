alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
input_letters = input()
for letter in alphabet:
    if letter not in input_letters:
        print(letter)
        break
