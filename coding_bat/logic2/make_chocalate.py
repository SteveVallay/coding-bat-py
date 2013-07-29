def make_chocolate(small,big,goal):
    a = goal/5
    b = goal%5
    if small < b:
        return -1
    elif big >= a:
        return b
    else:
        s=(a-big)*5 + b
        if s  > small:
            return -1
        else:
            return s

print make_chocolate(4,1,9)
print make_chocolate(4,1,10)
print make_chocolate(4,1,7)
