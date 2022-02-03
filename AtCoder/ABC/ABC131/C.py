import fractions
a,b,c,d = map(int,input().split())
lcm = c*d // fractions.gcd(c,d)
A = ((a-1) // c) + ((a-1) // d) - ((a-1) // lcm) 
B = (b // c) + (b // d) - (b // lcm)
ans = B-A
print(b-a+1-ans)