n,m = map(int,input().split())
a = [0] * m
b = [0] * m
for i in range(m):
    a[i],b[i] = map(int,input().split())
k = int(input())
c = list(map(int,input().split()))
graph = [[] for _ in range(m)]
for i in range(m):
    graph[a[i] - 1].append(b[i] - 1)
    graph[b[i] - 1].append(a[i] - 1)
print(*graph)