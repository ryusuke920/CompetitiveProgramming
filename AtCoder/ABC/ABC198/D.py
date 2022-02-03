from itertools import permutations
import sys
input = sys.stdin.readline
s1 = list(input().rstrip())
s2 = list(input().rstrip())
s3 = list(input().rstrip())

Type = set(s1 + s2 + s3)
if len(Type) > 10:
    exit(print("UNSOLVABLE"))

Type = list(Type)
# ダミー追加
for i in range(10 - len(Type)):
    Type.append(chr(65 + i))

cnt = [i for i in range(10)]

for i in permutations(cnt):
    num = {}
    for j in range(len(i)):
        num[F"{Type[j]}"] = i[j]
    x = y = z = 0
    Bool = True
    for j, k in enumerate(s1[::-1]):
        if x == 0 and k == "0":
            Bool = False
        x += num[k] * 10 ** j

    for j, k in enumerate(s2[::-1]):
        if y == 0 and k == "0":
            Bool = False
        y += num[k] * 10 ** j

    for j, k in enumerate(s3[::-1]):
        if z == 0 and k == "0":
            Bool = False
        z += num[k] * 10 ** j

    if Bool and x + y == z and len(str(x)) == len(s1) and len(str(y)) == len(s2) and len(str(z)) == len(s3) and x != 0 and y != 0 and z != 0:
        print(int(x))
        print(int(y))
        print(int(z))
        exit()

print("UNSOLVABLE")