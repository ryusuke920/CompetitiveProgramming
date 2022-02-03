n,m,l = map(int,input().split())
pqr = list(map(int,input().split()))
import itertools
ans = 0
for p,q,r in itertools.permutations(pqr):
    ans = max(ans, (n//p)*(m//q)*(l//r))
print(ans)