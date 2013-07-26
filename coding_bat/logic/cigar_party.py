def cigar_party(cigars,is_weekend):
    if is_weekend:
        return True
    elif 40 <= cigars <= 60:
        return True
    else:
        return False

print cigar_party(40,False)

