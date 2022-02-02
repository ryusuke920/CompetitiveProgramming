l = int(input())
n = int(input())
w = sorted(list(map(int,input().split())))
ans = 0
for i in range(n):
    ans += w[i]
    if ans > l:
        exit(print(i))
print(n)