N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

S_list = list((i,j) for i in range(N) for j in range(N) if S[i][j]=='#')
cntT = sum(1 for i in range(N) for j in range(N) if T[i][j]=='#')

if len(S_list)!=cntT :
	print("No")
	exit()

for _ in range(4):
	for i in range(-N+1,N):
		for j in range(-N+1,N):
			flag=True
			for x,y in S_list:
				if not (0<=x+i<N and 0<=y+j<N and T[x+i][y+j]=='#'):
					flag=False
					break  # <--重要
			if flag:
				print("Yes")
				exit()
	# rot
	S_list = [(y,N-1-x) for x,y in S_list]
print("No")