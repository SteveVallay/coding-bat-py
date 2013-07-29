def close_far(a,b,c):
    isb = abs(a-b) <=1
    isc = abs(a-c) <=1
    isa = abs(b-c) <=1
    s = 0
    if isa:
        s+=1
    if isb:
        s+=1
    if isc:
        s+=1
    if s <=1:
        return True
    else:
        return False

print close_far(1,2,10)
print close_far(1,2,3)
print close_far(4,1,3)
