def remove_exclamation_marks(s):
    for char in s :
        if '!' in s:
            return s.replace('!',"")
    return s