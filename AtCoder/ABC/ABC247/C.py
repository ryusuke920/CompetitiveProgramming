n = int(input())
ans = ['1']
for i in range(2, n + 1):
    ans.append(f"{ans[-1]} {str(i)} {ans[-1]}")

print(ans[-1], sep=' ')