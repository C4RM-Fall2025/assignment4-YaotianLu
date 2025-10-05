
def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = float(y) / float(ppy)
    c = float(face) * float(couponRate) / float(ppy)
    return c * (1 - (1 + r) ** -n) / r + face * (1 + r) ** -n
