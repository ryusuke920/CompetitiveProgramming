a,b,c = map(int,input().split())
n = a
mod = []
i = 2
if a == 1:
    print("YES")
    exit()
while True:
    if  a%b not in mod:
        mod.append(a%b)
        a += n
    else:
        print("NO")
        break
    i += 1
    if c in mod:
        print("YES")
        break