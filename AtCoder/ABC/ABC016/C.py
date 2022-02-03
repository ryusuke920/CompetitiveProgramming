n,m = map(int,input().split())
friend = [set() for _ in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    friend[a].add(b)
    friend[b].add(a)

for i in range(n):
    ans = set()
    for j in friend[i]:
        ans |= friend[j] # 自分以外の人が友達である人の合計
    ans -= (friend[i] | set([i])) # 自分が友達なのと自分自身は含めない
    print(len(ans))