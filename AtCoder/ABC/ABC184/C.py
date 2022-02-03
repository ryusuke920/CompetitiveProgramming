r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
ans = cnt = 0
p = abs(r2-r1) # マンハッタン距離
q = abs(c2-c1) # マンハッタン距離
if p == q == 0:
    print(0)
elif (p + q <= 3 or p == q):
    print(1)
elif ((p+q)%2 == 0 or p + q <= 6 or abs(p-q) <= 3):
    print(2)
else:
    print(3)