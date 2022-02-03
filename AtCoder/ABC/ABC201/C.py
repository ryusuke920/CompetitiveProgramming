#n = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
s = list(input())
num = [0] * 10 # 絶対、ない、５０
x = y = z = 0
if x >= 5:
    exit(print(0))
a,b,c = [], [], []
for i in range(10):
    if s[i] == "o":
        x += 1
        num[i] = 1
        a.append(i)
    elif s[i] == "x":
        num[i] = 2
        b.append(i)
        y += 1
    else:
        num[i] = 3
        c.append(i)
        z += 1
#print()
ans = cnt = 0
for i in range(0, 10000):
    word = str(i)
    ok = set()
    ng = set()
    ff = set()
    if len(str(i)) <= 3:
        word = "0" * (4 - len(str(i))) + word
    for j in range(4):
        if int(word[j]) in a:
            ok.add(int(word[j]))
        elif int(word[j]) in b:
            ng.add(int(word[j]))
        elif int(word[j]) in c:
            ff.add(int(word[j]))
    ff = list(ff)
    ng = list(ng)
    Bool = True
    for j in range(len(ng)):
        if int(ng[j]) in b:
            Bool = False
    #print(i,word,a,b,c,ok,ng,ff)
    if len(set(ok) ^ set(a)) == 0 and Bool == True:
        ans += 1
        #print(ok,ng,word,i)
print(ans)