a, b, c = map(int,input().split())
n = int(input())
print(max(0, n - a), max(0, 2 * n - b), max(0, 3 * n - c))