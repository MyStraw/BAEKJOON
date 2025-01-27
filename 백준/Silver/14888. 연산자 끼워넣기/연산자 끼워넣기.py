def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    
    max_result = -1e10
    min_result = 1e10

    def backtrack(idx, current, plus, minus, multiply, divide):
        nonlocal max_result, min_result
        if idx == N:
            max_result = max(max_result, int(current))
            min_result = min(min_result, int(current))
            return
        
        if plus:
            backtrack(idx + 1, current + nums[idx], plus - 1, minus, multiply, divide)
        if minus:
            backtrack(idx + 1, current - nums[idx], plus, minus - 1, multiply, divide)
        if multiply:
            backtrack(idx + 1, current * nums[idx], plus, minus, multiply - 1, divide)
        if divide:
            if current < 0:
                backtrack(idx + 1, -(-current // nums[idx]), plus, minus, multiply, divide - 1)
            else:
                backtrack(idx + 1, current // nums[idx], plus, minus, multiply, divide - 1)

    backtrack(1, nums[0], ops[0], ops[1], ops[2], ops[3])
    print(max_result)
    print(min_result)

if __name__ == "__main__":
    solve()