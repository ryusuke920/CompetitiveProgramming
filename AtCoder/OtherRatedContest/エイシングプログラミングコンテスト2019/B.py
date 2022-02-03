n = int(input())
a,b, = map(int,input().split())
p = list(map(int,input().split()))
cnt = [0]*3
for i in range(n):
    if p[i] <= a:
        cnt[0] += 1
    elif p[i] <= b:
        cnt[1] += 1
    else:
        cnt[2] += 1
print(min(cnt))