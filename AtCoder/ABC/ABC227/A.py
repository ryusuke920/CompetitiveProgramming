n, k, a = map(int,input().split())

ans = []
for i in range(a, a+k):
    if i % n == 0: ans.append(n)
    else: ans.append(i % n)

print(ans[-1])