n, k = map(int, input().split())
commands = [input().strip() for _ in range(n)]

ammo = 0
saved_ammo = None

for command in commands:
    if command == "ammo":
        ammo += k
    elif command == "shoot":
        ammo -= 1
    elif command == "save":
        saved_ammo = ammo
    elif command == "load":
        ammo = saved_ammo if saved_ammo is not None else 0
    print(ammo)