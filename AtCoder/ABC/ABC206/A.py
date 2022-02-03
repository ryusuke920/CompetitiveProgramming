n = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
import  math

if math.floor(1.08 * n) < 206:
    print("Yay!")
elif math.floor(1.08 * n) > 206:
    print(":(")
else:
    print("so-so")