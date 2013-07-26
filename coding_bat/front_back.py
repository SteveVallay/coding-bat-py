def front_back(ss):
    l=len(ss)
    if l==1:
        return ss
    elif l==2:
        return ss[1] + ss[0]
    else:
        return ss[l-1] + ss[1:l-1] + ss[0]
print front_back('a')
print front_back('sb')
print front_back('adcdef')
