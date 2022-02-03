n = int(input())
w = list(map(int,input().split()))
ans = 0
for i in range(n):
    ans += w[i]
    if ans >= sum(w)//2:
        print(min(abs(sum(w[:i+1])-sum(w[i+1:])), abs(sum(w[:i])-sum(w[i:]))))
        break