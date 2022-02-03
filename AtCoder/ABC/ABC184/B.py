#n = int(input())
n,x = map(int,input().split())
#a = list(map(int,input().split()))
ans = x
s = input()
for i in range(n):
    if s[i] == "o":
        ans += 1
    else:
        ans = max(0,ans-1)
print(ans)