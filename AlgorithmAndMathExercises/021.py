def combination(n, k):
    under = top = 1

    for i in range(2, k + 1):
        under *= i

    for i in range(k):
        top *= (n - i)

    nCk = top // under

    return nCk 

n, r = map(int, input().split())
print(combination(n, r))