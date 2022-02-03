#尺取り法
n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
if 0 in a:
    print(n)
    exit()
ans = cnt = 0
num = 1
for i in range(n):
    num *= a[i]
    if num <= k:
        ans = max(ans,i-cnt+1)
    else:
        num /= a[cnt]
        cnt += 1
print(ans)