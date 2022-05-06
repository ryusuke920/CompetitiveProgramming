n = int(input())
s = [input().split() for _ in range(n)]
bool = True
for i in range(n):
    check = [True, True]
    for j in range(2):
        name = s[i][j]
        for k in range(n):
            if i == k:
                continue
            if not (s[k][0] != name and s[k][1] != name):
                check[j] = False
        if not check[0] and not check[1]:
            bool = False

print('Yes') if bool else print('No')