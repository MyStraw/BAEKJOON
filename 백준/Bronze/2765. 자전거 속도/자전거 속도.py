pi = 3.1415927

trip = 1
while True:
    d, r, t = input().split()
    d = float(d)
    r = int(r)
    t = float(t)

    if r == 0:
        break

    circumference_inch = pi * d
    distance_inch = circumference_inch * r
    distance_mile = distance_inch / (12.0 * 5280.0)

    hours = t / 3600.0
    mph = distance_mile / hours

    print(f"Trip #{trip}: {distance_mile:.2f} {mph:.2f}")
    trip += 1