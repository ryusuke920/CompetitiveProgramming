s = input()
a, b = map(int, input().split())

ans = ''
for i in range(len(s)):
    if i == a - 1:
        ans += s[b - 1]
    elif i == b - 1:
        ans += s[a - 1]
    else:
        ans += s[i]

print(ans)