x = int(input())
import math
print(360*x//math.gcd(360,x)//x)