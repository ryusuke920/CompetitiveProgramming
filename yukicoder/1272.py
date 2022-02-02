from math import sin

k = int(input())
print(sum(sin(k * n) / n ** n for n in range(1, 11)))