n = int(input())
s = input()
ans = []
for i in range(n - 1):
    if s[i + 1] == 'J':
        ans.append(s[i])

print(*ans, sep='\n')