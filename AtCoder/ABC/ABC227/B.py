n = int(input())
s = list(map(int,input().split()))

ans = 0
for i in s:
    bool = False
    for a in range(1, 335):
        for b in range(1, 335):
            if i == 4 * a * b + 3 * a + 3 * b:
                bool = True

    if not bool: ans += 1

print(ans)