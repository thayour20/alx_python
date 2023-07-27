#!/usr/bin/env python3
def validate_password(password):
    if len(password) < 8:
        return (False)
    
    contain_upper = False
    contain_lower = False
    contain_digit = False

    for char in password:
        if char.isupper():
            contain_upper = True
        elif char.islower():
            contain_lower = True
        elif char.isdigit():
            contain_digit = True
    
    if not (contain_upper and contain_lower and contain_digit):
        return (False)
    if ' ' in password:
        return (False)
    return (True)