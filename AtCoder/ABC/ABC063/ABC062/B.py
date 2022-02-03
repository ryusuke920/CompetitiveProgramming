h,w = map(int,input().split())
a = [input() for i in range(h)]
x = "#"
for i in range(h+2):
    if i == 0 or i == h+1:
        print(x*(w+2))
    else:
        print(x,a[i-1],x,sep="")