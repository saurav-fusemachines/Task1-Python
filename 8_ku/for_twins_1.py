def type_validation(variable, _type): 
    if type(variable).__name__ == _type:
         return True
    else: 
        return False