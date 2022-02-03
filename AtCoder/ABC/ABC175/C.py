x,k,d = map(int,input().split())
x = abs(x)
num = x//d
if k >= num:
    x -= num*d
    cnt = k-num
else:
    x -= k*d
    print(x)
    exit()
if abs(x) > abs(x-d):
    x -= d
    cnt -= 1

if cnt%2 == 0:
    print(abs(x))
else:
    print(abs(abs(x)-abs(d)))