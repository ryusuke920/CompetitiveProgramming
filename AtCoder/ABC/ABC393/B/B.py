S = input()
N = len(S)

ans = 0
for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if j - i == k - j:
        if S[i] == "A":
          if S[j] == "B":
            if S[k] == "C":
              ans += 1
  
print(ans)