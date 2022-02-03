n = int(input())
#x, y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
cnt = 0
if sum(a) != sum(b):
    exit(print(-1))

if a == b:
    exit(print(0))

print(a)
print(b)