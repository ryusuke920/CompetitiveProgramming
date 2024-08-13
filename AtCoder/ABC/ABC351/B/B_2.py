N = int(input())

A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

print(A)
print(*A, sep="\n")