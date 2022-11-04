n = int(input())
s = bin(n)[2:]
print("0" * (10 - len(s)) + s)