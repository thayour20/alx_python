#!/usr/bin/env python3

def fibonacci_sequence(n):
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < n:
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fibonacci)
    return (fibonacci_list)
