import sys
input = sys.stdin.readline

def get_age(member):
    return member[0]

N = int(input())
members = []

for _ in range(N):
    age, name = input().split()
    members.append((int(age), name))

members.sort(key=get_age)

for age, name in members:
    print(age, name)
