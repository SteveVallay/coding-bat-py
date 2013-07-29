def sum13(nums):
    s = 0
    i = 0
    while i < len(nums):
        if nums[i] != 13:
            s += nums[i]
            i +=1
        else:
            i+=2
    return s

print sum13([1,13,4,2])
