n = int(input())
if n == 3:
    print(6, 10, 15)
else:
    ans = []
    for i in range(1, 10001):
        if i % 6 == 0 or i % 10 == 0 or i % 15 == 0:
            ans.append(i)
    print(*ans[:n])