n,q = map(int,input().split())
s = input()
cnt = [0]*n
for i in range(1,n):
    cnt[i] += cnt[i-1]
    if s[i-1:i+1] == "AC":
        cnt[i] += 1
for i in range(q):
    l,r = map(int,input().split())
    print(cnt[r-1] - cnt[l-1])