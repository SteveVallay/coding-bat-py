def array_count9(nums):
    s = 0
    for i in nums:
        if i == 9:
            s+=1
    return s

print array_count9([1,4,9,23,9])
