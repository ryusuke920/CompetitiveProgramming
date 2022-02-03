from collections import defaultdict

n, x = map(int,input().split())
a = list(map(int,input().split()))

emp_1 = defaultdict(int)

while not emp_1[x]:
    emp_1[x] += 1
    x = a[x - 1]

print(len(emp_1))