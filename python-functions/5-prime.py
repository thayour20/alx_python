#!/usr/bin/ env python3
def is_prime(number):
    if number <= 1:
        return (False)

    elif number == 2:
        return (True)
    elif number % 2 == 0:
        return (False)
    
    i = 3
    while i * i <= number:
        if number % i == 0:
            return (False)
        i += 2

    return (True) 
