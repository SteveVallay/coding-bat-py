def lucky_sum(a,b,c):
    l = [a,b,c]
    s = 0
    for i in l:
        if i == 13 :
            return s
        else:
            s += i
    return s
