from itertools import permutations
n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))

for i, j in enumerate(permutations(range(1, n + 1))):
    if j == p: a = i
    if j == q: b = i
print(abs(a - b))