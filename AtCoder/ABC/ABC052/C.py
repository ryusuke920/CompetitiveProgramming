n = int(input())
mod = 10**9 + 7

ans = []
def divisor(x):
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            ans.append(i)
            if i != x//i:
                ans.append(x//i)
    return ans

for i in range(2,n+1):
    divisor(i)
    print(i,ans)

from collections import Counter
x = Counter(ans)
print(x)