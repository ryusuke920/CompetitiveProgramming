h1,m1,h2,m2,k = map(int,input().split())
if m1 >= m2:
    H = (h2-h1-1)*60
    M = (60-(m1-m2))
else:
    H = (h2-h1)*60
    M = (m2-m1)
print(H+M-k)