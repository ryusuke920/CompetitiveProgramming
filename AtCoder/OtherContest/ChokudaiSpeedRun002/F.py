n = int(input())
ans = set([])
for _ in range(n):
    a,b = map(int,input().split())
    if b > a:
        a,b = b,a
    ans.add((a,b))
print(len(ans))