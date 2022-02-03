n = int(input())
def divisor(x):
    ans = []
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            ans.append(i)
            if i != x//i:
                ans.append(x//i)
    ans.sort()
    return ans

div = divisor(n)
for i in range(len(div)):
    print(div[i])