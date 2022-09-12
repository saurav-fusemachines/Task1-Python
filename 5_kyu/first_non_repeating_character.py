def first_non_repeating_letter(string):
    #your code here
    from collections import Counter
    
    counts = Counter(string.lower())
    for char in string:
        if counts[char.lower()]==1:
            return char
    return ''