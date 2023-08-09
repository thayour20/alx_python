#!/usr/bin/python 3
def best_score(a_dictionary):
    if best_score is None or not a_dictionary:
        return None
    
    best_key = None

    best_value = float("-inf")

    for key, value in a_dictionary.items():
        if value > best_value:
            best_key = key
            best_value = value

    return best_key
