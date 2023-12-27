class RollingHash:
    def __init__(self, s):
        self.base = 256  # 基数
        self.mod = 10**9 + 7  # 余り
        self.s = s
        self.n = len(s)
        self.hash_values_forward = [0] * (self.n + 1)
        self.hash_values_backward = [0] * (self.n + 1)
        self.calc_hashes()

    def calc_hashes(self):
        # 前方向のハッシュを計算
        base_power = 1
        for i in range(self.n):
            self.hash_values_forward[i + 1] = (self.hash_values_forward[i] * self.base + ord(self.s[i])) % self.mod
            base_power = (base_power * self.base) % self.mod

        # 後ろ方向のハッシュを計算
        base_power = 1
        for i in range(self.n - 1, -1, -1):
            self.hash_values_backward[i] = (self.hash_values_backward[i + 1] * self.base + ord(self.s[i])) % self.mod
            base_power = (base_power * self.base) % self.mod

    def get_forward_hash(self, l, r):
        return (self.hash_values_forward[r] - self.hash_values_forward[l] * pow(self.base, r - l, self.mod)) % self.mod

    def get_backward_hash(self, l, r):
        return (self.hash_values_backward[l] - self.hash_values_backward[r] * pow(self.base, r - l, self.mod)) % self.mod


def is_palindrome(s, l, r):
    return s.get_forward_hash(l, r) == s.get_backward_hash(l, r)


# メインの処理
N, Q = map(int, input().split())
S = input()

s = RollingHash(S)

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        x, c = map(str, query[1:])
        x = int(x) - 1
        S = S[:x] + c + S[x + 1:]
        s = RollingHash(S)
    elif query[0] == '2':
        L, R = map(int, query[1:])
        if is_palindrome(s, L - 1, R - 1):
            print("Yes")
        else:
            print("No")
