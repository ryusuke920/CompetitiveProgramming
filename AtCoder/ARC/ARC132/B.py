n = int(input())
p = list(map(int ,input().split()))

if p[0] == 1 and p[1] == 2:
    print(0)
else:
    print(min(p[0] + 1, n - p[0] + 1))