def end_other(a,b):
    la = len(a)
    lb = len(b)
    if la > lb:
        return a[-lb:].lower() == b.lower()
    else:
        return b[-la:].lower() == a.lower()

print end_other('abc','sdfABc')
print end_other('adfffffsdfabc','sdfABc')

