n,k = map(int,input().split())
def big(x):
    x = str(x)
    x = list(map(str,x))
    x.sort(reverse = True)
    word = ""
    for i in range(len(x)):
        word += x[i]
    if word == "":
        return 0
    else:
        return int(word)

def small(x):
    x = str(x)
    x = list(map(str,x))
    x.sort()
    word = ""
    ch = 1
    for i in range(len(x)):
        if ch == 1 and x[i] == "0": continue
        word += x[i]
        ch = 0
    if word == "":
        return 0
    else:
        return int(word)

ans = [0] * (k + 2)
ans[0] = n
for i in range(k):
    s = big(ans[i])
    t = small(ans[i])
    ans[i + 1] = s - t
print(ans[k])