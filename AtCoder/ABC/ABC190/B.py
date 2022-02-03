n,s,d = map(int,input().split())
for i in range(n):
    x,y = map(int,input().split())
    if y > d and x < s:
        exit(print("Yes"))
print("No")