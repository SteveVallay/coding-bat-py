def not_string(st):
    str_not = 'not'
    if st[0:3] == 'not':
        return st
    else:
        return 'not '+st


print not_string('good')
print not_string('not good')
