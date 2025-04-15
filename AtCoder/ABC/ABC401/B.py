N = int(input())
f = 0
ans = 0
for _ in range(N):
    S = input()
    if S == "login":
        f = 1
    if S == "logout":
        f = 0
    if S == "public":
        continue
    if S == "private":
        if f == 0:
            ans += 1

print(ans)
