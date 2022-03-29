n = int(input())
a = list(map(int, input().split()))
a = set(a)
for i in range(10000):
    if i not in a:
        exit(print(i))