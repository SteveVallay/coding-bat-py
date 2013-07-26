def array123(nums):
    has1 = False
    has2 = False
    has3 = False
    for i in nums:
        print 'i:',i
        if 1== i:
            has1 = True
        elif 2 == i:
            has2 = True
        elif 3==i :
            has3 = True

    if has1 and has2 and has3:
        return True
    else:
        return False
print array123([1,1,3,2])
print array123([1,1,4,2])
print array123([2,3,4,1])

