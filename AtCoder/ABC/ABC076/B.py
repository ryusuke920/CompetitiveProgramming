n=int(input())
k=int(input())
sum=1
for i in range(n):
    if sum+k > sum*2:
        sum*=2
    else:
        sum += k
print(sum)