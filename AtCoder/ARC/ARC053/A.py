h,w = map(int,input().split())
if h == 1 and w == 1:
    print(0)
elif h == 1:
    print(w-1)
elif w == 1:
    print(h-1)
else:
    print((h-1)*w+(w-1)*h)