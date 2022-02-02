test_case = [] # 入力例を受け取る配列

# ファイルの読み込み
with open("/Users/ryusuke/Documents/Atcoder/ICPCのwhile文対策のための標準入出力/input.txt", 'r') as f:
    for row in f:
        number = row.strip()
        test_case.append(number)

output= [] # 出力を格納する配列
# 実装したいコードを書く
# ここでは n の平方根を出力するコードを書く
x = int(number)**0.5
x.append(output)

# ファイルの書き込み
with open("/Users/ryusuke/Documents/output.txt", mode = 'w') as f:
    for i in range(len(output)):
        f.write(str(output[i]))