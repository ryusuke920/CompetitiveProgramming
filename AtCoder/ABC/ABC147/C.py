from itertools import product
n = int(input())
say = [[] for _ in range(n)]
a = []
for i in range(n):
    A = int(input())
    a.append(A)
    for j in range(A):
        x, y = map(int,input().split())
        say[i].append([x, y])

ans = 0
for i in product([0, 1], repeat = n):
    check = [True] * n
    Bool = True # 最初はTrue、反例ならFalseに途中で変更する

    for j in range(n):
        if i[j] == 1:
            check[j] = True # 正直者と仮定した場合はTrue
        else:
            check[j] = False # 不親切な人と仮定した場合はFalse

    for k in range(n):
        for l in range(a[k]):
            if check[k] == False: continue # 嘘をついている人は調べない
            if say[k][l][1] == 0 and check[say[k][l][0] - 1] == True:
                Bool = False
            elif say[k][l][1] == 1 and check[say[k][l][0] - 1] == False:
                Bool = False

    cnt = 0
    if Bool:
        for l in range(n):
            if check[l]:
                cnt += 1
    ans = max(ans, cnt)
print(ans)