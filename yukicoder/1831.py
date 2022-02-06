from collections import defaultdict

n = int(input())

a = [i + 1 for i in range(2 * n - 1)]
ans = []
d = defaultdict(int)
while True:
    