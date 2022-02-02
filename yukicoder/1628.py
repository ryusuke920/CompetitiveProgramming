n = int(input())
c = list(input().split())

num = ''
for i in reversed(range(9)):
    num += str((i + 1)) * int(c[i])

print(num)