a,b,c = map(int,input().split())
#a = list(map(int,input().split()))
ans = cnt = 0
if (a == b and b != c) or (b == c and c != a) or (a == c and b!= c):
    print("Yes")
else:
    print("No")