n, c = map(int,input().split())
a = [int(input()) for _ in range(n)]
ans = 10 ** 9
for i in range(1, 11):
    for j in range(1, 11):
        cnt = 0
        for k in range(n):
            if k % 2 == 0:
                if a[k] != i:
                    cnt += 1
            else:
                if a[k] != j:
                    cnt += 1
        if i != j:
            ans = min(ans, cnt * c)
print(ans)