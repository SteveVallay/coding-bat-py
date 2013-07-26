def pos_neg(a,b,neg):
    if not neg:
        if a*b < 0:
            return True
        else:
            return False
    else:
        if a < 0 and b < 0:
            return True
        else:
            return False
print pos_neg(-1,2,False)
print pos_neg(1,-2,False)
print pos_neg(-1,-2,True)

