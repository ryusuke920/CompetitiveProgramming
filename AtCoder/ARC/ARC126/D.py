n,m = map(int,input().split())
red = []
blue = []
for _ in range(m):
    a, b = map(int,input().split())
    red.append([a, 0])
    blue.append([b, 1])
red.sort(key=lambda x:x[1], reverse=True)
blue = sorted(blue)
ans = 0
for x_b in blue:
  for x_r in red:
    if x_r < x_b:
      red.remove([x_r, 0])
      ans += 1
      break
print(ans)