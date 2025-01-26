from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

queue = deque(A)
sub_queue = deque()
time = 0

while True:
    time += 1
    while len(sub_queue) < K and queue:
        student = queue.popleft()
        if student == 1:
            sub_queue.appendleft(student)
        else:
            sub_queue.append(student)

    if sub_queue and sub_queue[0] == sub_queue[-1]:
        sub_queue.popleft()
    else:
        if sub_queue:
            sub_queue.popleft()
        if sub_queue:
            sub_queue.pop()

    if not sub_queue and not queue:
        break

print(time)