a, b = map(int,input().split())
ans = 0
for i in range(b-a+1):
    ans += i 
print(ans-b)