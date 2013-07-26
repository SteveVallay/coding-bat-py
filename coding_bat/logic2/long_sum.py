def long_sum(a,b,c):
    s = 0
    if a == b:
        if a == c:
            return s
        else:
            s += c
            return s
    elif a == c:
        s += b
        return s
    else:
        if b == c:
            s+=a 
            return s
        else:
            s = a + b +c
            return s

print long_sum(1,2,1)
print long_sum(1,2,3)
print long_sum(1,2,2)

