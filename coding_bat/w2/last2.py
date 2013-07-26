def last2(str):
    l=len(str)
    s = 0
    if l <=2:
        return 1
    else:
        l2=str[l-2:]
        for i in range(l-1):
            print 'l2is:',l2
            print 'str[i:i+2]',str[i:i+2]
            if l2 == str[i:i+2]:
                s +=1
    return s
#print last2('hixxxhi')
#print last2('axxxaxx')
print last2('xxx')
