def pascal_triangle(n, k):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle[n-1][k-1]

n, k = map(int, input().split())
print(pascal_triangle(n, k))