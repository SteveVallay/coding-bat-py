def count_hi(str):
    l = len(str)
    s = 0
    for i in range(l-1):
        if str[i] == 'h' and str[i+1] == 'i':
            s+=1
    return  s

print count_hi('abc hi hi')
