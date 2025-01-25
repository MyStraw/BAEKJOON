N, M = map(int, input().split())

students = {}
for i in range(1, N + 1):
    students[i] = []

while True:
    cls, name = input().split()
    if cls == "0" and name == "0":
        break
    cls = int(cls)
    if len(students[cls]) < M:
        students[cls].append(name)

blue_team = []
white_team = []

for cls, names in students.items():
    names.sort(key=lambda x: (len(x), x))
    if cls % 2 == 1:
        blue_team.append((cls, names))
    else:
        white_team.append((cls, names))

blue_team.sort(key=lambda x: x[0])
white_team.sort(key=lambda x: x[0])

for cls, names in blue_team:
    for name in names:
        print(cls, name)

for cls, names in white_team:
    for name in names:
        print(cls, name)