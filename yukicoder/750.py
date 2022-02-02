n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: -x[0] / x[1])

for i in range(n):
    print(*ab[i])