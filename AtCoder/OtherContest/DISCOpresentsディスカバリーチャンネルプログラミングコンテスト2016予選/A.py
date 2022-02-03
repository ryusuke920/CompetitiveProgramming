n = int(input())
ch = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
if 51%n == 0:
    cnt = 51//n
else:
    cnt = 51//n+1
for i in range(cnt):
    print(ch[i*n:n*(i+1)])