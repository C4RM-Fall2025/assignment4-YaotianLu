def getBondPrice_E(face, couponRate, yc):
    face = float(face)
    couponRate = float(couponRate)
    c = face * couponRate
    price = sum(c / (1 + float(y)) ** (t + 1) for t, y in enumerate(yc))
    price += face / (1 + float(yc[-1])) ** len(yc)
    return price
