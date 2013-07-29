def centered_average(nums):
    ma = nums[0]
    mi = nums[0]
    s = 0
    l = len(nums)
    for i in range(l):
        ma=max(ma,nums[i])
        mi=min(mi,nums[i])
        s += nums[i]
    return (s-ma-mi)/(l-2)
        
        

print centered_average([1,4,2,3,5])
