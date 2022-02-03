s = int(input())
ans = []
ans.append(s)
while True:
    if s%2 == 0:
        s  = s//2
    else:
        s = s*3 + 1
    if s not in ans:
        ans.append(s)
    else:
        print(len(ans)+1)
        break