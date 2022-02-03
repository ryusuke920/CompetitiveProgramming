n = int(input())
a = [int(input()) for _ in range(n)]
print(n - len(set(a)))