def is_acceptable(password):
    vowels = set("aeiou")  
    has_vowel = any(c in vowels for c in password)
   
    count = 1
    for i in range(1, len(password)):
        if (password[i] in vowels) == (password[i-1] in vowels):
            count += 1
            if count >= 3:
                return False
        else:
            count = 1
  
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            if password[i] not in ('e', 'o'):
                return False
  
    return has_vowel

while True:
    pw = input().strip()
    if pw == 'end':
        break
    if is_acceptable(pw):
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
