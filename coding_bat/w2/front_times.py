def front_times(str,n):
    f=''
    if len(str) <=3:
        f=str
    else:
        f=str[0:3]
    return n*f
print front_times('abcdef',5)
