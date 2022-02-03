import fractions
a,b = map(int,input().split())
lcm = fractions.gcd(a,b)
print(a*b // lcm)