#!/usr/bin/env python3

def fibonacci_sequence(n):
    if n <= 0:
        return ([])
    elif n == 1:
        return ([0])

    fibonacci_list = [0, 1]
    for i in range(2, n):
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        if next_fibonacci < 0:
            return ([])
        fibonacci_list.append(next_fibonacci)
    return (fibonacci_list)
fibonacci_sequence(5)
print(fibonacci_sequence(20))