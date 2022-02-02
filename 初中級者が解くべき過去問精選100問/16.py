from itertools import permutations
n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
for i in range(n):
    p[i] -= 1
    q[i] -= 1
a = b = num = 0
for i in permutations(range(n)):
    if p == list(i):
        a = num
    if q == list(i):
        b = num
    num += 1
print(abs(a-b))