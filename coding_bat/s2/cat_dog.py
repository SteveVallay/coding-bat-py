def cat_dog(str):
    cat ='cat'
    dog ='dog'
    sc = 0
    sd = 0
    l = len(str)
    for i in range(l):
        print 'i=',i
        tmp = str[i:i+3]
        if tmp == cat :
            sc +=1
            #i+=3
        elif tmp == dog:
            sd +=1
            #i+=3
    if sc == sd:
        return True
    else:
        return False
print cat_dog('catdog')
