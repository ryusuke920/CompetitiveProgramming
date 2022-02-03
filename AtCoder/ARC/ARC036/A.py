n,k = map(int,input().split())
t = [int(input()) for _ in range(n)]
for i in range(n-2):
    ans = t[i] + t[i+1] + t[i+2]
    if ans < k:
        print(i+3)
        exit()
    ans = 0
else:
    print(-1)