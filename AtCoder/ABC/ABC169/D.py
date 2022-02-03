n = int(input())
if n == 1:
    print(0)
    exit()

def factorization(num):
    arr = []
    temp = num
    for i in range(2, int(num**0.5)+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([num, 1])

    return arr

x = factorization(n)
ans = 0
for i in range(len(x)):
  x[i][1] -= 1
  ans += 1
  y = 2
  while x[i][1] > 0:
    x[i][1] -= y
    if x[i][1] >= 0:
      ans += 1
    y += 1
print(ans)