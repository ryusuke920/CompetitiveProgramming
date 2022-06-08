n = int(input())
r = list(map(int, input().split()))
c = list(map(int, input().split()))

for _ in range(int(input())):
    y, x = map(int, input().split())
    y -= 1
    x -= 1
    if r[y] + c[x] >= n + 1:
        print('#', end= '')
    else:
        print('.', end= '')