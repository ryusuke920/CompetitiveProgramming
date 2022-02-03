n = int(input())
l = list(map(int,input().split()))

if max(l) >= sum(l) - max(l):
    print("No")
else:
    print("Yes")