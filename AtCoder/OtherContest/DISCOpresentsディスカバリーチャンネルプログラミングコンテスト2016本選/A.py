n = int(input())
Id = [int(input()) for _ in range(n)]
prize = [100000, 50000, 30000, 20000, 10000]
ans = [[0 ,0] for _ in range(n)]
for i in range(n):
    if Id[i] == 1:
        ans[i] = [i, prize[0]]
    elif Id[i] == 2:
        ans[i] = [i, prize[1]]
    elif Id[i] == 3:
        ans[i] = [i, prize[2]]
    elif Id[i] == 4:
        ans[i] = [i, prize[3]]
    elif Id[i] == 5:
        ans[i] = [i, prize[4]]
    else:
        ans[i] = [i, 0]
print(ans, sep = "\n")
ans.sort(key = lambda x: x[0])
for i in range(n):
    print(ans[i][1])