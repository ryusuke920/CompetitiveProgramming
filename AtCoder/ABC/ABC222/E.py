N,K = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(N)]
w = [[1]*K for _ in range(N)]
for i in range(N-2,-1,-1):
    x=[w[i+1][K-1]]*K
    for j in range(K-2,-1,-1):
        x[j]=(x[j+1]+w[i+1][j])%(10**9+7)
    j=k=0
    while j<K and k<K:
        if v[i][j]<=v[i+1][k]:
            w[i][j]=x[k]
            j+=1
        else:
            k+=1
    while j<K:
        w[i][j]=0
        j+=1
print(sum(w[0])%(10**9+7))
