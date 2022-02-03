l,r = map(int,input().split())
l = list(map(int,input().split()))
r = list(map(int,input().split()))
count = 0
for i in range(10,41):
    count += min(l.count(i),r.count(i))
print(count)