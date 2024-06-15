# Convert all numbers to strings.
# Define a custom comparator to decide the order based on the concatenated result.
# Sort the numbers using this custom comparator.
# Concatenate the sorted numbers to form the final result.

# Uses python3

import sys
from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

def largest_number(numbers):
    # Convert numbers to strings
    numbers = list(map(str, numbers))
    # Sort numbers using the custom comparator
    numbers.sort(key=cmp_to_key(compare))
    # Concatenate the sorted numbers
    return ''.join(numbers)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    n = int(data[0])
    numbers = data[1:]
    print(largest_number(numbers))