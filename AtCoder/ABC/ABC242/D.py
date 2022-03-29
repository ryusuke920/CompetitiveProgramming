s = input()
q = int(input())
len_ = len(s)

for _ in range(q):
    t, k = map(int, input().split())
    l = len_ * 2 ** t
    place = l // len_ + 1
    print(l, place)