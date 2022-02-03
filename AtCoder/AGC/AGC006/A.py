n = int(input())
s = input()
t = input()
t = t[::-1]
i = 0
for i in range(n):
    ch = t[i:]
    ch = ch[::-1]
    if ch in s:
        break
    else:
        i += 1
print(n+i)