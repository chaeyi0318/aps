def kmp(t, p):
    n = len(t)
    m = len(p)

    lps = [0] * (m+1)
    j= 0
    lps[0] = -1

    for i in range(1, m):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[m] = j