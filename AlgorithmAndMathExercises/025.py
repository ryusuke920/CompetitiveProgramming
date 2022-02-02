n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(sum(a) / 3 + 2 * sum(b) / 3)