def decode(string_):
    if type(string_) != str:
        return 'Input is not a string'
    letters = "abcdefghijklmnopqrstuvwxyz"
    translate = ""
    for l in string_:
        index = letters.find(l.lower())
        if l.isalpha() and l.islower():
            translate = translate + letters[::-1][index]
        elif l.isalpha() and l.isupper():
            translate = translate + letters[::-1][index].upper()
        else:
            translate = translate + l
    return translate