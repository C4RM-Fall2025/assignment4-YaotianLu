
def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy
    total = 0.0
    weighted = 0.0
    for i in range(1, n + 1):
        cf = c + (face if i == n else 0)
        pv = cf / ((1 + r) ** i)
        total += pv
        weighted += (i / ppy) * pv
    return weighted / total

