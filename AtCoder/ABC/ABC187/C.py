n = int(input())
s = set(input() for i in range(n))
for i in s:
    if "!" + i in s:
        exit(print(i))
print("satisfiable")