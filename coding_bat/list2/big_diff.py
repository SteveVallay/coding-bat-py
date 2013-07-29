def big_diff(nums):
    l = len(nums)
    ma = nums[0]
    mi = nums[0]
    for i in range(l-1):
        ma = max(ma,nums[i+1])
        mi = min(mi,nums[i+1])

    return ma - mi

print big_diff([10,3,5,6])

