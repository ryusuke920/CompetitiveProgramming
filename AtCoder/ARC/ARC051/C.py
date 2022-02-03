n, a, b = map(int,input().split())
p = sorted(list(map(int,input().split())))
mod = 10 ** 9 + 7
print(p)
if a == 1:
    print(*p, sep = "\n")