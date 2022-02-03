n = int(input())
#x,y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
ans = 1
for i in range(2,n+1):
    if i == 6 or i == 8 or i == 12 or i == 14 or i == 15 or i == 16 or i == 18 or i == 20 or i == 21 or i == 22 or i == 24 or i == 25 or i == 26 or i == 27 or i == 28 or i == 30: continue
    ans *= i

if n == 30:
    ans *= 2

print(ans + 1)