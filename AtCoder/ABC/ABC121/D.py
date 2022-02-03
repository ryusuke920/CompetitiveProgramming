a, b = map(int,input().split())
# print(len(bin(10 ** 12)))  -> 40桁
if a == b:
    print(a)
elif a % 2 == 0 and b % 2 == 0:
    x = (b - a) // 2 # 偶数ペアの個数
    if x % 2 == 0:
        print(b)
    elif x % 2 == 1:
        print(b ^ 1)
elif a % 2 == 1 and b % 2 == 0:
    x = (b - a + 1 - 2) // 2 # 偶数ペアの個数
    if x % 2 == 0:
        print(a ^ b)
    elif x % 2 == 1:
        print(a ^ b ^ 1)
elif a % 2 == 0 and b % 2 == 1:
    x = (b - a + 1) // 2 # 偶数ペアの個数
    if x % 2 == 0:
        print(0)
    elif x % 2 == 1:
        print(1)
elif a % 2 == 1 and b % 2 == 1:
    x = (b - a) // 2 # 偶数ペアの個数
    if x % 2 == 0:
        print(a)
    elif x % 2 == 1:
        print(a ^ 1)