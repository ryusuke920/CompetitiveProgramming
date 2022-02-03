n = int(input())
a = list(map(int,input().split()))
for i in a:
    print(f"{int(bin(i)[2:]):05}")