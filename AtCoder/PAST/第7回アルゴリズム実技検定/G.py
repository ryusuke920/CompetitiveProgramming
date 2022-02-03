n = int(input())
ans = []
i = 0
while n > 0:
    if n % 3 == 1:
      ans.append(1)
      n -= 1
    elif n % 3 == 2:
      n -= 2
      ans.append(-1)
    elif n % 3 == 0:
      ans.append(3 ** i)
    i += 1
    n -= 3 ** i

ans.append(3 ** i)

if n % 3 == 0:
  print(len(ans) - 1)
  print(*ans[1:])
else:
  print(len(ans))
  print(*ans)