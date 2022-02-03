#n = int(input())
a,b,c,d = map(int,input().split())
#a = list(map(int,input().split()))
if (c<=a and a <= d) or (a <= c  and c<= b):
    print("Yes")
else:
    print("No")