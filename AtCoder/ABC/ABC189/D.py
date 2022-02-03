n = int(input())
cnt = 0
for i in range(n):
    s = input()
    if s == "OR":
        cnt += 2 ** (i + 1)
print(cnt + 1)