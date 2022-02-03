n = list(map(int,input().split()))
ans = 0
count = 0
for i in range(5):
    if n[i] == 0:
        print(i+1)