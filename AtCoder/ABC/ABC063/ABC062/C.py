p,q = map(int,input().split())

if p%3 == 0 or q%3 == 0:
    print(0)
    exit()

def two(h,w):
    # 縦（横）に２回分割する場合
    x = min(h,w)
    # 縦横に１回ずつ分割する場合
    if w == 2:
        w1 = w2 = 1
    else:
        w1 = w//3+1
        w2 = w//3
    if h == 2:
        h1 = h2 = 1
    else:
        h1 = h//2+1
        h2 = h//2
    # 4回場合分け
    # h1 and w1
    a1 = w1*h
    a2 = (w-w1)*h1
    a3 = (w-w1)*(h-h1)
    a4 = max(a1,a2,a3) - min(a1,a2,a3) 
    # h1 and w2
    b1 = w2*h
    b2 = (w-w2)*h1
    b3 = (w-w2)*(h-h1)
    b4 = max(b1,b2,b3) - min(b1,b2,b3) 
    # h2 and w1
    c1 = w1*h
    c2 = (w-w1)*h2
    c3 = (w-w1)*(h-h2)
    c4 = max(c1,c2,c3) - min(c1,c2,c3) 
    # h2 and w2
    d1 = w2*h
    d2 = (w-w2)*h2
    d3 = (w-w2)*(h-h2)
    d4 = max(d1,d2,d3) - min(d1,d2,d3)
    return min(a4,b4,c4,d4,x)

s = two(p,q)
t = two(q,p)

print(min(s,t))