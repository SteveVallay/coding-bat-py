def xyz_there(str):
    if str[0:3] == 'xyz':
        return True
    for i in range(len(str)):
        if xyz_match(str[i:]):
            return True
    return False

def xyz_match(s):
    if len(s) <4 :
        return False
    elif s[0] !='.' and s[1:4] == 'xyz':
        return True
    else:
        return False
print xyz_there('abcxyz')
print xyz_there('abc.xyz')
