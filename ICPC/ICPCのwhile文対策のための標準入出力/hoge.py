output = []
with open("/Users/ryusuke/Documents/input.txt", 'r') as f:
    for row in f:
        x = row.strip()
        x = list(map(int,x.split()))
        output.append(x)
output = output[:-2]

ans = []
for i in range(0,len(output),2):
    x = output[i]
    y = output[i+1]
    ans.append(x[0]*y[1] - x[1]*y[0])

with open("/Users/ryusuke/Documents/output.txt", mode = 'w') as f:
    for i in range(len(ans)):
        f.write(str(ans[i]) + "\n")