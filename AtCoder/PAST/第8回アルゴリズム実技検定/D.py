x, y = map(int,input().split())
def divisors(n):
    divisor = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i)
            if i != n // i:
                divisor.append(n // i)

    divisor.sort()
    return divisor

a = divisors(x)
b = divisors(y)

if len(a) == len(b):
    print("Z")
elif len(a) > len(b):
    print("X")
else:
    print("Y")