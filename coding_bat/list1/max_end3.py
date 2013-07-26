def max_end3(nums):
    a=0
    if nums[0] > nums[-1]:
        a = nums[0]
    else:
        a = nums[-1]
    return [a]*3

print max_end3([1,3,2])


