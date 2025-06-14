from collections import Counter
import sys
from math import comb

input = sys.stdin.read

def main():
    data = input().split()
    S = data[0]
    N = int(data[1])
    handles = data[2:]
  
    freq = Counter(handle[0] for handle in handles)    
 
    s_freq = Counter(S)
    letters = list(s_freq.keys())

    if len(letters) == 1:
        c = s_freq[letters[0]]
        count = comb(freq[letters[0]], c) if freq[letters[0]] >= c else 0
    elif len(letters) == 2:       
        a, b = letters
        if s_freq[a] == 2:
            count = comb(freq[a], 2) * freq[b] if freq[a] >= 2 and freq[b] >= 1 else 0
        else:
            count = comb(freq[b], 2) * freq[a] if freq[b] >= 2 and freq[a] >= 1 else 0
    else:       
        a, b, c = letters
        count = freq[a] * freq[b] * freq[c]

    print(count)

main()
