n = int(input())
s = input()
num = s.count("R")*s.count("G")*s.count("B")
cnt = 0
for i in range(n):
        for j in range(i+1,n):
            if 0 <= 2*j-i < n:
                if s[i] != s[j] and s[j] != s[2*j-i] and s[2*j-i] != s[i]:
                    cnt += 1
print(num - cnt)