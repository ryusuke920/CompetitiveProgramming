#n = int(input())
x,y = map(str,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
for i in range(len(x)):
    ans += int(x[i])
for i in range(len(y)):
    cnt += int(y[i])
print(max(ans,cnt))