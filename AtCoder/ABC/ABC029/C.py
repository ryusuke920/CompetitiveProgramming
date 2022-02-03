from itertools import product
n = int(input())
for i in product("abc", repeat = n):
    print("".join(i))