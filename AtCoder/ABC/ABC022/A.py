a,b,c = map(int,input().split())
d = int(input())
ans = 0
e=[ int(input()) for i in range(a-1)]
if (b <= d <= c):
    ans+=1
for i in range(a-1):
    d += e[i]
    if(b <= d <= c):
        ans += 1
print(ans)