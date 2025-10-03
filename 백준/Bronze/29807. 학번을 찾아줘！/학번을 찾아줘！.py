import sys

data = list(map(int, sys.stdin.read().split()))

t = data[0]
scores = data[1:1 + t]
while len(scores) < 5:
    scores.append(0)
scores = scores[:5]

korean, math, english, inquiry, second_foreign = scores

korean_part = abs(korean - english) * (508 if korean > english else 108)
math_part = abs(math - inquiry) * (212 if math > inquiry else 305)
foreign_part = second_foreign * 707

student_id = (korean_part + math_part + foreign_part) * 4763

print(student_id)
