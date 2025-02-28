x, y, z = map(int, input().split())
x_p, y_p, z_p = map(int, input().split())

if x_p == x and y_p == y and z_p == z:
    print("A")
elif y_p == y and z_p == z and x_p >= x / 2:
    print("B")
elif y_p == y and z_p == z:
    print("C")
elif z_p == z and y_p >= y / 2:
    print("D")
else:
    print("E")