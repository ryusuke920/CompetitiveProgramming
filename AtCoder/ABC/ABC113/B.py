n = int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
ch = [10000]*n
for i in range(n):
    ch[i] = abs(a - (t - h[i]*6/1000))
print(ch.index(min(ch))+1)