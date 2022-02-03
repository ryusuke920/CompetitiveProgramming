n = int(input())
#x, y = map(int,input().split())
#a = list(map(int,input().split()))
s = input()
ans = cnt = 0

for i in range(n):
    if s[i] == "1":
        if i % 2 == 0:
            print("Takahashi")
            exit()
        else:
            exit(print("Aoki"))

#print("Aoki")