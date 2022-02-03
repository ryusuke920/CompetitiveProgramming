n = int(input())

ans = []
for _ in range(n):
    l = list(map(int,input().split()))
    ans.append(l)

ans = list(map(list,set(map(tuple, ans))))

print(len(ans))