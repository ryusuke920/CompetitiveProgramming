n,k = map(int,input().split())
p = list(map(int,input().split()))
num = [(i+1) for i in p]
ans = sum(num[:k])
ch = ans
for i in range(n-k):
    ch += num[i+k] - num[i]
    ans = max(ans, ch)
print(ans/2)