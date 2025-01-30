def main():
    n = int(input())
    wires = []
    for _ in range(n):
        a, b = map(int, input().split())
        wires.append((a, b))
    
    wires.sort()
    b_list = [b for a, b in wires]
    
    dp = []
    for b in b_list:
        if not dp or dp[-1] < b:
            dp.append(b)
        else:
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] >= b:
                    right = mid - 1
                else:
                    left = mid + 1
            if left < len(dp):
                dp[left] = b
    
    print(n - len(dp))

if __name__ == "__main__":
    main()