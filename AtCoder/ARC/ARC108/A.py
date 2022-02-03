#n = int(input())
s, p = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
for n in range(1, int(p**0.5) + 1):
    m = s - n
    if n*m == p:
        exit(print("Yes"))
print("No")