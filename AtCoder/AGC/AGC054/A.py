n = int(input())
s = input()
if s[0] != s[-1]:
    print(1)
else:
    for i in range(n - 1):
        if s[0] != s[i + 1] and s[0] != s[i]:
            print(2)
            break
    else:
        print(-1)