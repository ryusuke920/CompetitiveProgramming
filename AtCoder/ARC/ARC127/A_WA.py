def solve(num: int):
    global ans
    if int(num) > n: return
    for i in range(10):
        num = str(num)
        if int(num + str(i)) <= n:
            if i == 1:
                ans += len(num) + 1
                solve(num + str(i))
            else:
                ans += len(num)

ans = 1
n = int(input())
solve("1")
print(ans)