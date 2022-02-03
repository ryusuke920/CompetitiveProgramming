n = int(input())
a = list(map(int,input().split()))
count = [0]*n
for i in range(n):
    count[a[i]-1] += 1
ans = 0
for i in range(n):
    ans += count[i]*(count[i]-1)//2
for i in a:
    before = count[i-1]*(count[i-1]-1)//2
    after = (count[i-1]-1)*(count[i-1]-2)//2
    print(ans - before + after)