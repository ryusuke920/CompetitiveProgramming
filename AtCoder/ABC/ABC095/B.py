n,x = map(int,input().split())
m = [int(input()) for i in range(n)]
m.sort()
print((x - sum(m))//m[0] + n)