def make_bricks(small,big,goal):
    a = goal/5
    b = goal%5
    if big >= a and small >= b:
        return True
    elif big < a:
        return (a-big)*5+b <=small
    else:
        return False

print make_bricks(3,1,8)
print make_bricks(3,1,9)
print make_bricks(3,2,10)

