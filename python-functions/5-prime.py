#!/usr/bin/ env python3
def is_prime(number):
    prime = True
    if number <= 0:
        prime = False
    elif number > 1:

        for i in range (2, number):
            if number % i == 0:
                prime = False
                break
    return (prime)