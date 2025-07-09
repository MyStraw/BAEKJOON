def solution(babbling):
    def bab(s):
        words = ["aya", "ye", "woo", "ma"]
        i = 0
        last = ""

        while i < len(s):
            match = False
            for word in words:
                if s[i:i+len(word)] == word and word != last:
                    i += len(word)
                    last = word
                    match = True
                    break
            if not match:
                return False
        return True

    count = 0
    for i in babbling:        
        if bab(i):  
            count += 1
    return count