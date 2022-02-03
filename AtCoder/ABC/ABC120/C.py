s = str(input()) 
zero = s.count("0")
one = s.count("1")
print(min(zero,one)*2)