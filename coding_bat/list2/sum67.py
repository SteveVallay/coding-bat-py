def sum67(nums):
    start = False
    s = 0
    i = 0
    while i < len(nums):
        if start == False:
            if nums[i] != 6:
                s+= nums[i]
            else:
                start = True
                pass
        else:
            if nums[i] != 7:
                pass
            else:
               start=False 
        i +=1

    return s


print sum67([1,2,3,6,3,4,7,1])



