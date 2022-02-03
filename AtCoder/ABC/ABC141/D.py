import heapq
n,m = map(int,input().split())
a = list(map(lambda x: int(x)*(-1),input().split()))
heapq.heapify(a) #aを優先度付きキューにする
for _ in range(m):
    tmp = heapq.heappop(a)
    heapq.heappush(a,(-1)*(-tmp//2)) #負のままだと切り捨てが切り上げになる！
print((-1)*sum(a))