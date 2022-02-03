ans = []
now = []
for _ in range(int(input())):
    s = input()
    if s == 'READ':
        ans.append(now[-1])
        now.pop()
    else:
        now.append(s)

print(*ans, sep='\n')