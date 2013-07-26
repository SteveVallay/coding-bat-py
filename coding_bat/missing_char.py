def missing_char(stra,n):
    l=len(stra)
    if l < n:
        return None
    return stra[:n] + stra[n+1:] 

print missing_char('abcd',3)
