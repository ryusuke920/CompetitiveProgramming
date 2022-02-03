a,b,k = map(int,input().split())
count = 0
if b >= a:
    count = a
    a = b
    b = count
ch = 1
for i in range(a,0,-1):
    if a % i == 0 and b % i == 0 and k == ch:
        print(i)
        break
    elif a % i == 0 and b % i == 0:
        ch += 1