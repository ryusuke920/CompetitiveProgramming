n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())

ans = set()
for i in t:
    ans.add(i)

for i in s:
    if i in ans:
        print('Yes')
    else:
        print('No')