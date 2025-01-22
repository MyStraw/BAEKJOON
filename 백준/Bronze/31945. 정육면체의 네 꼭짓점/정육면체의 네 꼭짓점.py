cube_points = [
    (0,0,0), (0,0,1), (0,1,0), (0,1,1),
    (1,0,0), (1,0,1), (1,1,0), (1,1,1)
]

def same_face(points):
    x_same = all(p[0] == points[0][0] for p in points)
    y_same = all(p[1] == points[0][1] for p in points)
    z_same = all(p[2] == points[0][2] for p in points)
    return x_same or y_same or z_same

def check(indices):
    points = [cube_points[i] for i in indices]
    return same_face(points)

T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    points = [a, b, c, d]
    print("YES" if check(points) else "NO")