n = int(input())
s = input()

def LCS(s1, s2):
    l1, l2 = len(s1), len(s2)
    if l1 == 0 or l2 == 0: return ''

    # memorization of m[l1][l2]
    m = []
    for x in range(l1):
        m.append([0]*(l2))

    # Fill 0th row
    isSameFound = False
    for i in range(l1):
        if isSameFound or s1[i] == s2[0]:
            m[i][0] = 1
            isSameFound = True

    # Fill 0th column
    isSameFound = False
    for j in range(l2):
        if isSameFound or s2[j] == s1[0]:
            m[0][j] = 1
            isSameFound = True

    max_len = 0
    # m[i][j] stores the maximum length of subsequence of s1[:i+1], s2[:j+1]
    for i in range(0, l1-1):
        for j in range(0, l2-1):
            if s1[i+1] == s2[j+1]:
                m[i+1][j+1] = m[i][j] + 1
                max_len = max(m[i][j], max_len)
            else:
                m[i+1][j+1] = max(m[i][j+1], m[i+1][j])

    #If you want to know just the length of the lcs, return maxLen.
    #Here we'll try to print the lcs.
    lcs_str = ''
    i, j = l1-1, l2-1
    while i >= 0 and j >= 0:
        if s1[i] == s2[j]:
            lcs_str += s1[i] #or s2[j-1]
            i -= 1
            j -= 1
        else:
            if m[i-1][j] > m[i][j-1]:
                i -= 1
            else:
                j -= 1

    return lcs_str[::-1]

ans = 0
for i in range(1, len(s)):
    before = s[: i]
    after = s[i :]
    word = LCS(before, after)
    ans = max(ans, len(word))
print(n - ans * 2)