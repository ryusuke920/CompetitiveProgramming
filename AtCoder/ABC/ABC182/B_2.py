n = int(input())
a = list(map(int,input().split()))
print([sum(j%i==0 for j in a)for i in range(2,1001)].index(max([sum(j%i==0 for j in a)for i in range(2,1001)]))+2)