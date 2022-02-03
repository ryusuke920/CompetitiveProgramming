judge = [True] * 6
ans = [0] * 6

for i in range(int(input())):
    p, v = input().split()
    if v == 'WA': continue

    if p == 'A' and judge[0]:
        judge[0] = False
        ans[0] = i + 1

    if p == 'B' and judge[1]:
        judge[1] = False
        ans[1] = i + 1

    if p == 'C' and judge[2]:
        judge[2] = False
        ans[2] = i + 1

    if p == 'D' and judge[3]:
        judge[3] = False
        ans[3] = i + 1

    if p == 'E' and judge[4]:
        judge[4] = False
        ans[4] = i + 1

    if p == 'F' and judge[5]:
        judge[5] = False
        ans[5] = i + 1

print(*ans, sep='\n')