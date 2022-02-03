a,b = map(int,input().split())
ans = 1000
for i in range(-4,5):
    for j in range(-8,9):
        for k in range(-41,40):
            if a + i*10 + j*5 + k == b:
                ans = min(ans, abs(i)+abs(j)+abs(k))
print(ans)