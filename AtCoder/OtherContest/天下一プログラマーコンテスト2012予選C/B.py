s = input()
ans = []

# S
S = []
Bool = [False] * 5
if s.count("S10") >= 1:
    if s.count("SJ") >= 1:
        if s.count("SQ") >= 1:
            if s.count("SK") >= 1:
                if s.count("SA") >= 1:
                    i = 0
                    while True:
                        if i >= len(s) - 1:
                            break

                        if s[i] + s[i + 1] + s[i + 2] == "S10":
                            Bool[0] = True
                            i += 2
                        elif s[i] + s[i + 1] == "SJ":
                            Bool[1] = True
                            i += 1
                        elif s[i] + s[i + 1] == "SQ":
                            Bool[2] = True
                            i += 1
                        elif s[i] + s[i + 1] == "SK":
                            Bool[3] = True
                            i += 1
                        elif s[i] + s[i + 1] == "SA":
                            Bool[4] = True
                            i += 1
                        else:
                            S.append(s[i])
                        
                        judge = True
                        for j in range(5):
                            if not Bool[j]:
                                judge = False
                                break
                        if judge:
                            ans.append([S, len(S)])
                            break
                        i += 1

# H
i = 0
H = []
Bool = [False] * 5
if s.count("H10") >= 1:
    if s.count("HJ") >= 1:
        if s.count("HQ") >= 1:
            if s.count("HK") >= 1:
                if s.count("HA") >= 1:
                    i = 0
                    while True:
                        if i >= len(s) - 1:
                            break

                        if s[i] + s[i + 1] + s[i + 2] == "H10":
                            Bool[0] = True
                            i += 2
                        elif s[i] + s[i + 1] == "HJ":
                            Bool[1] = True
                            i += 1
                        elif s[i] + s[i + 1] == "HQ":
                            Bool[2] = True
                            i += 1
                        elif s[i] + s[i + 1] == "HK":
                            Bool[3] = True
                            i += 1
                        elif s[i] + s[i + 1] == "HA":
                            Bool[4] = True
                            i += 1
                        else:
                            S.append(s[i])
                        
                        judge = True
                        for j in range(5):
                            if not Bool[j]:
                                judge = False
                                break
                        if judge:
                            ans.append([H, len(H)])
                            break
                        i += 1

# D
i = 0
D = []
Bool = [False] * 5
if s.count("D10") >= 1:
    if s.count("DJ") >= 1:
        if s.count("DQ") >= 1:
            if s.count("DK") >= 1:
                if s.count("DA") >= 1:
                    i = 0
                    while True:
                        if i >= len(s) - 1:
                            break

                        if s[i] + s[i + 1] + s[i + 2] == "D10":
                            Bool[0] = True
                            i += 2
                        elif s[i] + s[i + 1] == "DJ":
                            Bool[1] = True
                            i += 1
                        elif s[i] + s[i + 1] == "DQ":
                            Bool[2] = True
                            i += 1
                        elif s[i] + s[i + 1] == "DK":
                            Bool[3] = True
                            i += 1
                        elif s[i] + s[i + 1] == "DA":
                            Bool[4] = True
                            i += 1
                        else:
                            S.append(s[i])
                        
                        judge = True
                        for j in range(5):
                            if not Bool[j]:
                                judge = False
                                break
                        if judge:
                            ans.append([D, len(D)])
                            break
                        i += 1

# C
i = 0
C = []
Bool = [False] * 5
if s.count("C10") >= 1:
    if s.count("CJ") >= 1:
        if s.count("CQ") >= 1:
            if s.count("CK") >= 1:
                if s.count("CA") >= 1:
                    i = 0
                    while True:
                        if i >= len(s) - 1:
                            break

                        if s[i] + s[i + 1] + s[i + 2] == "C10":
                            Bool[0] = True
                            i += 2
                        elif s[i] + s[i + 1] == "CJ":
                            Bool[1] = True
                            i += 1
                        elif s[i] + s[i + 1] == "CQ":
                            Bool[2] = True
                            i += 1
                        elif s[i] + s[i + 1] == "CK":
                            Bool[3] = True
                            i += 1
                        elif s[i] + s[i + 1] == "CA":
                            Bool[4] = True
                            i += 1
                        else:
                            S.append(s[i])
                        
                        judge = True
                        for j in range(5):
                            if not Bool[j]:
                                judge = False
                                break
                        if judge:
                            ans.append([C, len(C)])
                            break
                        i += 1

ans.sort(key = lambda x: x[1])

if ans[0][1] == 0:
    print(0)
else:
    print(*ans[0][0], sep = "")