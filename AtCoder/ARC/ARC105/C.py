n,m = map(int,input().split())
w = list(map(int,input().split()))
w.sort()
l = [0]*m #長さ
v = [0]*m #耐久値
for i in range(m):
    l[i],v[i] = map(int,input().split())
#print(w)
weima = max(w)
#-1のパターン
for i in range(m):
    if weima > v[i]:
        print(-1)
        exit()

#耐久値の最も低い場所とその耐久値
vmi = min(v)
nu = v.index(vmi)
lmi = l[nu]

#1番長い長い所とその耐久値
lma = max(l)
nu = l.index(lma)
vma = v[nu]

i = 1
#１番低いところに耐えれる分Wを結合
while True:
    if len(w) == 1:
        break
    if w[0]+w[-i] <= vma:
        tmp = w[0]+w[-i]
        w.pop(-i)
        w[0] = tmp
        i -= 1
        vma = vmi
    w.sort()
    #print(w)
    if len(w) == 1:
        break
    i += 1
    if w[0] == w[-i]:
        break
print(min((len(w)-2)*lma+lmi,(len(w)-1)*lma))