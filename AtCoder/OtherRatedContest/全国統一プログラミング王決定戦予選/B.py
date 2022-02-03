n = int(input())
a = input()
b = input()
c = input()
cnt = 0
for i in range(n):
    if a[i] != b[i] and b[i] != c[i] and c[i] != a[i]:
        cnt += 2
    elif a[i] == b[i] == c[i]:
        cnt += 0
    else:
        cnt += 1
print(cnt)