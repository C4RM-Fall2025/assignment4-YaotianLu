

def getBondPrice_E(face, couponRate, yc):
    c = float(face) * float(couponRate)
    bondprice = 0.0
    for t, y in enumerate(yc, start=1):
        price += c / (1 + float(y))**t
    bondprice += float(face) / (1 + float(yc[-1]))**len(yc)
    return bondprice

