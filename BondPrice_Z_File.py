def getBondPrice_Z(face, couponRate, times, yc):
    if len(times) != len(yc):
        raise ValueError("times and yc must have same length")
    c = float(face) * float(couponRate)
    price = sum(c / (1 + float(y))**float(t) for t, y in zip(times, yc))
    price += float(face) / (1 + float(yc[-1]))**float(times[-1])
    return price
