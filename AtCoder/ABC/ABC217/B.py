contest = ["ABC", "ARC", "AGC", "AHC"]
s = [input() for _ in range(3)]
print(*(set(contest) ^ set(s)))