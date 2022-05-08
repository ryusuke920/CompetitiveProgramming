def f1(n: int):
    return 2 * (l1 + l2) * n

def f2(n: int):
    return 2 * (l2 + l3) * n

def f3(n: int):
    return 2 * (l1 + l3) * n

l1, l2, l3 = map(int, input().split())
a, b, c = map(int, input().split())

ans = []
ans.append(f1(a) + f2(b) + f3(c))
ans.append(f1(a) + f2(c) + f3(b))
ans.append(f1(b) + f2(a) + f3(c))
ans.append(f1(b) + f2(c) + f3(a))
ans.append(f1(c) + f2(a) + f3(b))
ans.append(f1(c) + f2(b) + f3(a))

print(min(ans))