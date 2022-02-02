from collections import defaultdict

def factorization(n):
    arr = []
    tmp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))

top = a[0] * b[-1]
down = 1
for i in a:
    down *= i

for i in b:
    down *= i
down //= (a[0] * b[-1])

f_1 = factorization(top)
f_2 = factorization(down)

d_1 = defaultdict(int)
d_2 = defaultdict(int)

for i, j in f_1:
    d_1[i] = j
for i, j in f_2:
    d_2[i] = j

ans_top = defaultdict(int)
ans_down = defaultdict(int)

for k, v in d_1.items():
    if d_2[k] == 0:
        ans_top[k] = v
    else:
        ans_top[k] = v - min(v, d_2[k])

for k, v in d_2.items():
    if d_2[k] == 0:
        ans_down[k] = v
    else:
        ans_down[k] = v - min(v, d_1[k])

'''
print(top, down)
print(f_1, f_2)
print(d_1, d_2)
print(ans_top, ans_down)
'''

multi_top, multi_down = 1, 1
for k, v in ans_top.items():
    multi_top *= k ** v

for k, v in ans_down.items():
    multi_down *= k ** v

print(multi_top, multi_down)