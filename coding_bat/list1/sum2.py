def sum2(nums):
    l = len(nums)
    s=0
    if l == 0:
        return 0
    elif l ==1:
        return nums[0]
    else:
        for i in range(2):
            s+= nums[i]
        return s

print sum2([1,2,2])
