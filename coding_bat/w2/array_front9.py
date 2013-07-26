def array_front9(array):
    l = len(array)
    if l==0:
        return False
    for i,v in enumerate(array):
        if v==9:
            return True
        elif i==3 or i>= l-1:
            return False

print array_front9([1,3,4])
print array_front9([1,2,4,3,4])
print array_front9([])

