n = int(input())
num = [0] * n
for i in range(n):
    num[int(input()) - 1] += 1
if 0 in num:
    print(num.index(2) + 1, num.index(0) + 1)
else:
    print("Correct")