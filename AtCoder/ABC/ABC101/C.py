n,k = map(int,input().split())
a = list(map(int,input().split()))
ans = k
count = 1
while ans < n:
    ans += k-1
    count += 1
print(count)