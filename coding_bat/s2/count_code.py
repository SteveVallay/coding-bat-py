def count_code(str):
    s = 0
    for i in range(len(str)-3):
        if equal_code(str[i:]):
            s+=1
    
    return s

def equal_code(str):
    if str[:2] == 'co' and str[3] == 'e':
        return True
    else:
        return False
print count_code('adfacodeasdfcofe')
