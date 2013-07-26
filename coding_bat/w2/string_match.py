def string_match(a,b):
    la = len(a)
    lb = len(b)
    l = min(la,lb)
    s = 0
    for i in range(0,l-1):
        print 'ai+2', a[i:i+2]
        if a[i:i+2] == b[i:i+2]:
            s+=1
    return s


def min(a,b):
    if a > b:
        return b
    else:
        return a




print string_match('abcdef','abdcef')
