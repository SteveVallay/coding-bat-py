def string_splosion(str):
    l = len(str)
    i = 0
    s=''
    while i <= l:
       s+=str[0:i]
       i+=1

    return s

print string_splosion('ABCD')
