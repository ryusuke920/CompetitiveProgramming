n = int(input())
import sys
input = sys.stdin.readline
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
for i in range(n):
    t = int(input())
    if t % 4 == 2:
        print("Same")
    elif t%2 == 1:
        print("Odd")
    else:
        print("Even")