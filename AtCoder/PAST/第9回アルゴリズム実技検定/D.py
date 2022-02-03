n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

student = []
for i in range(n):
    student.append((a[i] + b[i], a[i], i + 1))

student.sort(key=lambda x: (-x[0], -x[1], x[2]))

ans = []
for i in range(n):
    ans.append(student[i][2])

print(*ans)