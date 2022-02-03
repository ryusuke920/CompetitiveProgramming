s = input()
t = input()
cnt = 0
while True:
    if s == t:
        break
    s = s[-1] + s[:-1]
    cnt += 1
    if cnt >= 2000:
        cnt = -1
        break
print(cnt)