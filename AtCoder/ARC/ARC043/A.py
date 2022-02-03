n,a,b = map(int,input().split())
s = [int(input()) for _ in range(n)]
if max(s) - min(s) != 0:
    p = b/(max(s)-min(s))
else:
    exit(print(-1))
q = a - p*(sum(s)/n)
print(p,q)