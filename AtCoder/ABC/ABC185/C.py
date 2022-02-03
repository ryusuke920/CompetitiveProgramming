n = int(input())
import math
a = math.factorial(n - 1)
b = math.factorial(11)
c = math.factorial(n - 12)
print(a // (b * c))