n,m = map(int,input().split())
people = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    (a, b) = (a - 1, b - 1)
    people[a].append(b)
    people[b].append(a)

for i in range(n):
    ans = set()
    for j in people[i]:
        ans |= set(people[j])
    ans -= set([i] + people[i])
    print(len(ans))