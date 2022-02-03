h = int(input())
w = int(input())
n = int(input())
if h >= w and n%h != 0:
    print(n//h+1)
elif h >= w and n%h == 0:
    print(n//h)
elif w >= h and n%w != 0:
    print(n//w+1)
else:
    print(n//w)