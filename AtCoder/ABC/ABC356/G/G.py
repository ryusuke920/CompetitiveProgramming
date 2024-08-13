def calculate_floor_sum(N, A):
    from collections import defaultdict
    
    # 要素の出現回数を数える
    count = defaultdict(int)
    for num in A:
        count[num] += 1
    
    total_sum = 0
    
    # 各要素 A_j について計算
    for j in range(N):
        a_j = A[j]
        if a_j == 0:
            continue
        
        # 0.5 * a_j 以上の要素の数を数える
        for a_i in count:
            if a_i <= a_j and a_i >= 0.5 * a_j:
                total_sum += count[a_i]
        
        # 自分自身を除く
        total_sum -= 1
    
    # 計算結果を半分にする（各ペアが2回ずつ数えられているため）
    total_sum //= 2
    
    return total_sum

# 入力の例
N = int(input())
A = list(map(int, input().split()))
result = calculate_floor_sum(N, A)
print(result)