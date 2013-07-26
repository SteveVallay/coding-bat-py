def front3(str):
    front=''
    if len(str) < 3:
        front=str
    else:
        front=str[:3]
        
    return 3*front
print front3('abcd')
print front3('a')

