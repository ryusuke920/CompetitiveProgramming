n = int(input())
h = list(map(int,input().split()))
ch = h[0]
for i in range(n-1):
    if ch > h[i+1] + 1:
        print("No")
        exit()
    ch = max(ch,h[i+1])
print("Yes")