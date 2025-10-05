
 def getBondPrice(y, face, couponRate, m, ppy=1):
    n = m * ppy
    r = y / ppy
    c = face * couponRate / ppy
    bondPrice = c * (1 - (1 + r) ** -n) / r + face * (1 + r) ** -n
    return bondPrice
