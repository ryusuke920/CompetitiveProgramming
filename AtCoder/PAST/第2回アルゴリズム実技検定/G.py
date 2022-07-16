from collections import deque, defaultdict

q = deque()
l = 0

for _ in range(int(input())):

    query = list(input().split())
    if query[0] == '1':
        q.append((query[1], int(query[2])))
        l += int(query[2])
    elif query[0] == '2':
        d = defaultdict(int)
        pop_num = int(query[1])
        if l <= pop_num:
            while q:
                char, num = q.popleft()
                d[char] += num
                l = 0
        elif l > pop_num:
            while pop_num > 0:
                char, num = q.popleft()
                if pop_num - num >= 0:
                    d[char] += num
                    l -= num
                    pop_num -= num
                else:
                    d[char] += pop_num
                    q.appendleft((char, num - pop_num))
                    l -= pop_num
                    pop_num = 0
        
        ans = 0
        for k, v in d.items():
            ans += v ** 2
        
        print(ans)