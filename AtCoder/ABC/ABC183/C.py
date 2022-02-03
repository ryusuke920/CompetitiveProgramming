n,k = map(int,input().split())
num = [i+2 for i in range(n-1)]
t = [list(map(int,input().split())) for _ in range(n)]
import itertools
ans = 0
for i in itertools.permutations(num):
    cnt = 0
    for j in range(len(i)):
        if j == 0:
            cnt += t[0][i[j]-1]
        else:
            cnt += t[i[j-1]-1][i[j]-1]
        #print(i,j,i[j],cnt)
    cnt += t[i[-1]-1][0]
    if cnt == k:
        ans += 1
print(ans)