n,k,s = map(int,input().split())
if s == 10**9:
    ans1 = [s]*k
    ans2 = [1]*(n-k)
    ans = ans1 + ans2
else: # s < 10**9
    ans1 = [s]*k
    ans2 = [s+100]*(n-k)
    ans = ans1 + ans2
print(*ans)